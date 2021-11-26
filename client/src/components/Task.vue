<template>
  <li
    @click="updateStatus(pk, status)"
    class="list-group-item d-flex align-items-center justify-content-between noselect"
    :class="{ strike: status }"
  >
    {{ task }}
    <button
      @click="delTask(pk)"
      class="btn btn-outline-secondary btn-highlight"
      type="button"
      id="button-addon2"
    >
      <i class="fas fa-minus-circle plusbtn"></i>
    </button>
  </li>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Task',
  props: ['task', 'status', 'pk'],
  methods: {
    delTask(pk) {
      axios
        .delete('http://localhost:8000/api/task-delete/' + pk + '/')
        .then(() => {
          this.$emit('deleted')
        })
        .catch((error) => {
          console.log(error)
        })
    },
    updateStatus(pk, status) {
      axios
        .put('http://localhost:8000/api/task-update/' + pk + '/', {
          id: pk,
          task: this.task,
          completed: !status,
        })
        .then(() => {
          this.$emit('updated')
        })
    },
  },
}
</script>

<style scoped>
.plusbtn {
  font-size: 1.5rem;
  color: #e76f51;
}
.btn-highlight:hover {
  background-color: #e9c46a;
  color: #fff;
}

.strike {
  text-decoration: line-through;
}

li {
  padding: 10px 20px;
  box-shadow: 0 3px 10px rgb(0 0 0 / 0.2);
  margin: 10px 0px;
  width: 100%;
}

li:hover {
  cursor: pointer;
  width: 99%;
}

.noselect {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Old versions of Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently
                                  supported by Chrome, Edge, Opera and Firefox */
}
</style>
