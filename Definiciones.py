"""
Plantilla básica para Definiciones.
Autor: Danttez
"""
pregunta = (
        "Dime, ¿cuál de las siguientes definiciones quieres conocer primero?\n"
        "a) Git Init\nb) Git Push\nc) Git Add\nd) Git Commit\n"
        "Selecciona una: "
        )
respuesta = input(pregunta).strip().lower()

if respuesta in ("a", "git init"):
    print("Nos permite inicializar un repositorio local en una carpeta.")
elif respuesta in ("b", "git push"):
    print("Envía tus cambios al repositorio remoto (por ejemplo, GitHub).")
elif respuesta in ("c", "git add"):
    print("Agrega archivos al 'staging area', preparándolos para ser confirmados.")
elif respuesta in ("d", "git commit"):
    print("Confirma los cambios añadidos, creando un punto en el historial del proyecto.")
else:
    print("No escogiste una opción válida.")