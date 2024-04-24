from PIL import Image
import os

def convert_image(input_path, output_path, output_format):
    try:
        with Image.open(input_path) as img:
            if img.mode in ['RGBA', 'P']:
                img = img.convert('RGB')
            img.save(output_path, format=output_format)
        print(f"Imagem convertida e salva como: {output_path}")
    except Exception as e:
        print(f"Erro ao converter a imagem: {e}")

def convert_all_images(source_folder, output_folder, output_format):
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(source_folder, filename)
            output_filename = f"{os.path.splitext(filename)[0]}.{output_format.lower()}"
            output_path = os.path.join(output_folder, output_filename)
            convert_image(input_path, output_path, output_format)

def compress_all_images(source_folder, output_folder, quality=85):
    for filename in os.listdir(source_folder):
        # Identifica a extensão original do arquivo e prepara o caminho de entrada e saída
        ext = filename.lower().rsplit('.', 1)[-1]
        input_path = os.path.join(source_folder, filename)
        output_filename = f"{os.path.splitext(filename)[0]}.{ext}"
        output_path = os.path.join(output_folder, output_filename)

        try:
            with Image.open(input_path) as img:
                # Converte imagens com canal alpha para 'RGB' se for salvar como JPEG
                if ext == 'jpg' or ext == 'jpeg':
                    if img.mode == 'RGBA' or img.mode == 'P':
                        img = img.convert('RGB')
                    img.save(output_path, 'JPEG', quality=quality)
                elif img.mode == 'RGBA' and (ext == 'png' or ext == 'gif'):
                    img.save(output_path, ext.upper(), optimize=True)
                else:
                    # Salva o arquivo mantendo o formato original
                    img.save(output_path, ext.upper())
            print(f"Imagem comprimida e salva como: {output_path}")
        except Exception as e:
            print(f"Erro ao comprimir a imagem: {e}")

def main():
    print("Selecione a opção desejada:")
    print("1. Converter")
    print("2. Comprimir")
    choice = input("Digite a opção desejada: ")

    if choice == '1':
        sub_choice = input("Deseja converter uma imagem específica (digite 1) ou todas as imagens na pasta (digite 2)? ")
        if sub_choice == '1':
            image_name = input("Digite o nome da imagem (inclua a extensão, por exemplo, imagem.jpg): ")
            input_path = f'converter/{image_name}'
            if not os.path.exists(input_path):
                print("Imagem não encontrada, tente novamente.")
                return
            print("Selecione o formato para conversão:")
            print("1. PNG")
            print("2. JPG")
            print("3. WEBP")
            format_choice = input("Digite o número do formato: ")
            format_dict = {'1': 'PNG', '2': 'JPEG', '3': 'WEBP'}
            if format_choice in format_dict:
                output_format = format_dict[format_choice]
                output_path = f'convertidas/{os.path.splitext(image_name)[0]}.{output_format.lower()}'
                convert_image(input_path, output_path, output_format)
            else:
                print("Escolha inválida, tente novamente.")
        elif sub_choice == '2':
            print("Convertendo todas as imagens da pasta 'converter'...")
            print("Selecione o formato para conversão de todas as imagens:")
            print("1. PNG")
            print("2. JPG")
            print("3. WEBP")
            format_choice = input("Digite o número do formato: ")
            format_dict = {'1': 'PNG', '2': 'JPEG', '3': 'WEBP'}
            if format_choice in format_dict:
                output_format = format_dict[format_choice]
                convert_all_images('converter', 'convertidas', output_format)
            else:
                print("Escolha inválida, tente novamente.")
    elif choice == '2':
        print("Comprimindo todas as imagens na pasta 'comprimir'...")
        compress_all_images('comprimir', 'comprimidas')
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()
