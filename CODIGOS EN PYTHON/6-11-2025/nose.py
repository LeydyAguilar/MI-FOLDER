from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def inicializar():
    glClearColor(0.1, 0.1, 0.1, 1.0)  # Fondo gris oscuro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-4.4, 4.4, -4.4, 4.4)  # 🔹 Ampliamos el rango visible

def dibujar_texto(x, y, texto, r=1.0, g=1.0, b=1.0):
    """Dibuja texto en pantalla con color RGB"""
    glColor3f(r, g, b)
    glRasterPos2f(x, y)
    for ch in texto:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch))

def dibujar_ecuacion():
    glClear(GL_COLOR_BUFFER_BIT)

    # Ejes coordenados
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-4.4, 0.0)
    glVertex2f(4.4, 0.0)
    glVertex2f(0.0, -4.4)
    glVertex2f(0.0, 4.4)
    glEnd()

    # Etiquetas de los ejes
    dibujar_texto(4.1, -0.25, "X", 1.0, 0.8, 0.2)
    dibujar_texto(-0.2, 4.1, "Y", 1.0, 0.8, 0.2)

    # Marcas y valores del eje X
    for i in range(-4, 5):
        glBegin(GL_LINES)
        glVertex2f(i, -0.08)
        glVertex2f(i, 0.08)
        glEnd()
        if i != 0:
            dibujar_texto(i - 0.1, -0.35, str(i))

    # Marcas y valores del eje Y
    for j in range(-4, 5):
        glBegin(GL_LINES)
        glVertex2f(-0.08, j)
        glVertex2f(0.08, j)
        glEnd()
        if j != 0:
            dibujar_texto(0.15, j - 0.15, str(j))

    # Dibujar la parábola y = x^2 (recortada para no salir del rango)
    glColor3f(0.2, 0.8, 1.0)
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-2.1, 2.1, 400):
        y = x ** 2
        glVertex2f(x, y)
    glEnd()

    # Título
    dibujar_texto(-1.2, 4.2, "Grafica de y = x^2", 0.8, 1.0, 0.6)

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"COORDENADAS - OpenGL (Leydy - Rango -4.4 a 4.4)")
    inicializar()
    glutDisplayFunc(dibujar_ecuacion)
    glutMainLoop()

if __name__ == "__main__":
    main()

