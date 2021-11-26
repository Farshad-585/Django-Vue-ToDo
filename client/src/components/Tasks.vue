<template>
  <section class="task-container">
    <div class="task">
      <TaskInput @taskAdded="getTasks" />
      <ul>
        <Task
          v-for="task in tasks"
          :key="task.id"
          :task="task.task"
          :status="task.completed"
          :pk="task.id"
          @updated="getTasks"
          @deleted="getTasks"
        >
        </Task>
      </ul>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
import TaskInput from './TaskInput.vue'
import Task from './Task.vue'

export default {
  name: 'Tasks',
  data() {
    return {
      tasks: [],
    }
  },
  methods: {
    getTasks() {
      axios
        .get('http://localhost:8000/api/task-list')
        .then((response) => {
          this.tasks = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  created() {
    this.getTasks()
  },
  components: {
    TaskInput,
    Task,
  },
}
</script>

<style scoped>
.task-container {
  width: 100%;
  height: 93vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.task {
  width: 90%;
  height: 80%;
  background-color: #ffffff;
  border-radius: 10px;
  padding: 30px 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

ul {
  list-style: none;
  padding: 20px 0px;
  margin: 0;
  width: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
