import qrcode


def generar_qr_codigo(enlace, nombre_archivo='codigo_qr.png'):
    # Crear objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Añadir el enlace al código QR
    qr.add_data(enlace)
    qr.make(fit=True)

    # Crear una imagen del código QR
    img = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen en un archivo
    img.save(nombre_archivo)


if __name__ == "__main__":
    # Solicitar al usuario que ingrese el enlace web
    enlace_web = input("Ingrese el enlace web para convertir a QR: ")

    # Generar el código QR y guardar la imagen
    generar_qr_codigo(enlace_web)

    print("El código QR se ha generado exitosamente en el archivo 'codigo_qr.png'.")
