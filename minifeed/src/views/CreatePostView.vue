<template>
    <div>
      <h1>Create Post</h1>
      <form @submit.prevent="createPost">
        <textarea rows="15" placeholder="Text" v-model="text" />
  
        <button type="submit">Create</button>
      </form>
    </div>
  </template>
  
  
<script setup>
    import { ref } from "vue"
    import { useAxios } from "@/composables/useAxios";
    import { useToast } from "vue-toast-notification";

    const { post } = useAxios()
    const $toast = useToast()

    const text = ref("")

    const createPost = () => {
      post("/posts/", { text: text.value })
        .then((response) => {
          console.log(response);
          text.value = "";
        })
        .catch((error) => {
          if (error.response) {
            const status = error.response.status;

            if (status === 401) {
              $toast.error("You need to login first!", { position: "bottom" });
            } else {
              $toast.error("An unexpected error occurred.", { position: "bottom" });
            }
          } else {
            $toast.error(
              "Unable to reach the server. Please check your connection.",
              {
                position: "bottom",
              }
            );
          }
        });
};
</script>
  
<style lang="scss" scoped>
  textarea {
    display: block;
    width: 100%;
    min-width: 300px;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 25px;
    border-radius: 8px;
    padding: 10px;
    font-size: 1rem;
    border: 1px solid $border-default;
    background-color: $background-secondary;
    color: $text-primary;
  }

  textarea::placeholder {
    font-size: 1rem;
    color: $text-secondary;
  }

  button {
    background: green; // Cor de fundo principal do botão
    color: $text-on-primary; // Cor do texto sobre o fundo principal do botão
    border: none;
    padding: 10px;
    width: 325px;
    font-size: 1rem;
    cursor: pointer;
    border-radius: 4px;
  }
</style>

  