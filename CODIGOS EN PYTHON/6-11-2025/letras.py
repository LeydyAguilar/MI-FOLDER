from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Texto blanco
    glRasterPos2f(-0.2, 0.1)  # Posición (un poco arriba del centro)
    for ch in "Hola Mundo":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

    glRasterPos2f(-0.8, -0.1) 
    for ch in "Soy Leydy,yo soy del departamento de Puno":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 300)
    glutCreateWindow(b"PyOpenGL - Hola Leydy")
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()




    
    

