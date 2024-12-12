<template>
  <div class="pagination">
    <span
      class="pagination-item"
      :class="{ 'pagination-item-active': i === modelValue }"
      @click="changePage(i)"
      v-for="i in pages"
      :key="`page-${i}`"
    >
      {{ i }}
    </span>
  </div>
</template>

<script setup>
  // Define as props que são passadas para o componente
  defineProps({
    modelValue: {
      type: Number,
      required: true,
    },
    pages: {
      type: Number,
      required: true,
    },
  });

  // Define o emit para atualizar o valor de modelValue
  const emit = defineEmits(["update:modelValue"]);

  // Função para mudar a página ao clicar
  function changePage(page) {
    if (page !== modelValue) { // Verifica se a página clicada é diferente da atual
      emit("update:modelValue", page);
    }
  }
</script>

<style lang="scss" scoped>
  .pagination {
    text-align: center;
    margin-top: 20px;
  }

  .pagination-item {
    padding: 5px 10px;
    margin: 0 5px 10px 5px;
    font-size: 1.5rem;
    cursor: pointer;
    border-radius: 4px;
    color: red;
  }

  .pagination-item-active {
    background-color: palevioletred;
    color: greenyellow;
  }
</style>



