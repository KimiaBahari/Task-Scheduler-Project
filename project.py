import schedule
import time
from datetime import datetime
from plyer import notification

class TaskScheduler:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name, task_time):
        self.tasks[task_name] = task_time
        print(f"Task '{task_name}' scheduled for {task_time}.")

    def remove_task(self, task_name):
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' removed.")
        else:
            print(f"Task '{task_name}' not found.")

    def list_tasks(self):
        if self.tasks:
            print("Scheduled Tasks:")
            for task_name, task_time in self.tasks.items():
                print(f"{task_name} - {task_time}")
        else:
            print("No tasks scheduled.")

    def run(self):
        while True:
            current_time = datetime.now().strftime("%H:%M")
            for task_name, task_time in list(self.tasks.items()):
                if current_time == task_time:
                    self.notify_task(task_name)
                    self.remove_task(task_name)

            time.sleep(60)  # Check tasks every minute

    def notify_task(self, task_name):
        notification_title = "Task Reminder"
        notification_message = f"It's time to do '{task_name}'!"
        notification.timeout = 10  # Notification timeout in seconds
        notification.notify(
            title=notification_title,
            message=notification_message,
        )

def main():
    print("Task Scheduler App")
    scheduler = TaskScheduler()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Start Scheduler")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            task_time = input("Enter task time (HH:MM): ")
            scheduler.add_task(task_name, task_time)
        elif choice == "2":
            task_name = input("Enter the task name to remove: ")
            scheduler.remove_task(task_name)
        elif choice == "3":
            scheduler.list_tasks()
        elif choice == "4":
            scheduler.run()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
