from PIL import Image
import os

def convert_image(input_path, output_path, output_format):
    try:
        with Image.open(input_path) as img:
            # Verifica se a imagem está no modo 'RGBA' ou 'P' e converte para 'RGB'
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

def main():
    choice = input("Deseja converter uma imagem específica (digite 1) ou todas as imagens na pasta (digite 2)? ")
    
    if choice == '1':
        image_name = input("Digite o nome da imagem (inclua a extensão, por exemplo, imagem.jpg): ")
        input_path = f'toConvert/{image_name}'

        if not os.path.exists(input_path):
            print("Imagem não encontrada, tente novamente.")
            return

        print("Selecione o formato para conversão:")
        print("1. PNG")
        print("2. JPG")
        print("3. WEBP")
        format_choice = input("Digite o número do formato: ")

        format_dict = {
            '1': 'PNG',
            '2': 'JPEG',
            '3': 'WEBP'
        }

        if format_choice in format_dict:
            output_format = format_dict[format_choice]
            output_path = f'converted/{os.path.splitext(image_name)[0]}.{output_format.lower()}'
            convert_image(input_path, output_path, output_format)
        else:
            print("Escolha inválida, tente novamente.")
    
    elif choice == '2':
        print("Convertendo todas as imagens da pasta 'toConvert'...")
        print("Selecione o formato para conversão de todas as imagens:")
        print("1. PNG")
        print("2. JPG")
        print("3. WEBP")
        format_choice = input("Digite o número do formato: ")

        format_dict = {
            '1': 'PNG',
            '2': 'JPEG',
            '3': 'WEBP'
        }

        if format_choice in format_dict:
            output_format = format_dict[format_choice]
            convert_all_images('toConvert', 'converted', output_format)
        else:
            print("Escolha inválida, tente novamente.")
    else:
        print("Opção inválida, por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()
