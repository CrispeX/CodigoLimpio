from rich import console
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()
class Tarea:
    def __init__(self, titulo:str, descripcion:str, prioridad:str):
        self.titulo = titulo
        self.descripcion = descripcion
        self.__completada: bool = False
        self.fecha_creacion: datetime = datetime.now()
        self.prioridad = prioridad

    def marcar_completado(self) -> None:
        """ Se marca una tarea no completada
        """
        self.__completada = True

    @property
    def estado(self) -> None:
        return "Tarea completada" if self.__completada else "Tarea no completada"

class GestorTareas:
    def __init__(self):
        self.__tareas: list[Tarea] = []

    def agregar_tarea(self, tarea: Tarea) -> None:
      """Agrega una tarea al gestor de tareas
      """
      self.__tareas.append(tarea)
      console.print(f"[bold green] Exito:[/bold green] Se ha agregado la tarea {tarea.titulo} agregada")

    def eliminar_tarea(self, tarea: Tarea) -> None:
      """Elimina una tarea del gestor de tareas
      """
      self.__tareas.remove(tarea)

    def mostrar_tareas(self) -> None:
      """Muestra las tareas del gestor de tareas
      """
      table = Table(title="mi primer tablero de tareas")
      table.add_column("Titulo", style="cyan")
      table.add_column("Estado", justify="Center")
      table.add_column("Descripcion", style="magenta")
      table.add_column("Fecha de creacion", justify="Right")
      table.add_column("Prioridad", justify="Right")

      for tarea in self.__tareas:
        table.add_row(tarea.titulo,
                      tarea.estado,
                      tarea.descripcion,
                      tarea.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S"),
                      tarea.prioridad)
      console.print(table)

mi_gestor = GestorTareas()
#crear tareas
tarea_calculo = Tarea("Calculo", "derivada","Alta")
tarea_algebra = Tarea("Algebra", "ecuaciones","Baja")

mi_gestor.agregar_tarea(tarea_calculo)
mi_gestor.agregar_tarea(tarea_algebra)
mi_gestor.eliminar_tarea(tarea_algebra)

tarea_calculo.marcar_completado()
mi_gestor.mostrar_tareas()