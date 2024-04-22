import boto3
import os


def create_data_folder():
    try:
        os.makedirs('data', exist_ok=True)
        print("Carpeta 'data' creada exitosamente.")
    except Exception as e:
        print(f"Error al crear la carpeta 'data': {e}")


def download_data_from_s3(bucket_name, remote_path, local_path):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, remote_path, local_path)
        print(f"Datos descargados desde {bucket_name}/{remote_path} a {local_path}")
    except Exception as e:
        print(f"Error al descargar datos desde S3: {e}")


if __name__ == "__main__":
    bucket_name = 'proyecto-final-gab-cris-manu'
    remote_path = 'data_from_scientists/heart.csv'
    local_path = 'data/heart.csv'

    create_data_folder()
    download_data_from_s3(bucket_name, remote_path, local_path)