const app = new Vue({
    el: '#app',
    data: {
        newTask: '',
        tasks: []
    },
    computed: {
        totalTasks() {
            return this.tasks.length;
        },
        completedTasks() {
            return this.tasks.filter(task => task.completed).length;
        }
    },
    methods: {
        addTask() {
            if (this.newTask.trim() === '') return;
            this.tasks.push({ id: Date.now(), text: this.newTask, completed: false });
            this.newTask = '';
            
        },
        toggleComplete(taskId) {
            const task = this.tasks.find(task => task.id === taskId);
            task.completed = !task.completed;
        },
        deleteTask(taskId) {
            this.tasks = this.tasks.filter(task => task.id !== taskId);
        }
    }
});

