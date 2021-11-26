<template>
  <div class="input-group mb-3 pd-5 task-input">
  <input type="text" class="form-control" placeholder="Add Task" aria-label="Recipient's username" aria-describedby="button-addon2" v-model="task">
  <button @click="addTask" class="btn btn-outline-secondary btn-highlight" type="button" id="button-addon2"><i class="fas fa-plus-circle plusbtn"></i></button>
</div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'TaskInput',
  data() {
    return {
      task: ''
    }
  },
  methods: {
    addTask() {
      axios.post('http://localhost:8000/api/task-create/', {
        task: this.task
    }).then(() => {
        this.task = '';
        this.$emit('taskAdded');
    }).catch(error => {
        console.log(error);
    });
    }  
  }
}
</script>

<style scoped>
.plusbtn{
  font-size: 1.5rem;
  color: #264653;

}
.btn-highlight:hover{
  background-color: #2a9d8f;
  color: #fff;
}

.task-input {
  width: 70%;
  /* padding-bottom: 30px; */
  box-shadow: 0 3px 10px rgb(0 0 0 / 0.2);
}

</style>