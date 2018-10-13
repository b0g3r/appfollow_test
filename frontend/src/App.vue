<template>
  <sui-container text>
    <sui-header size="huge">AppFollow Permission Requester 2000</sui-header>

    <sui-form>
      <sui-segment stacked>
        <sui-form-field>
          <sui-input
            placeholder="https://play.google.com/store/apps/details?id=org.telegram.messenger&hl=en"
            icon="cloud download"
            icon-position="left"
            v-model="url"
          ></sui-input>
        </sui-form-field>
        <sui-button
          :loading="loading"
          size="large"
          color="teal"
          @click.prevent="requestPermission"
          fluid
        >Запросить разрешения приложения</sui-button>

      </sui-segment>
      <sui-segment stacked>
        <sui-message v-if="errors" color="red" icon="bug">
          <template v-for="(errors, key) in errors">
            <span> {{ key }}</span>
            <ul v-for="error in errors">
              <li>{{ error }}</li>
            </ul>
          </template>
        </sui-message>
        <template v-if="permissions">
          <permissions
            :blocks="permissions"
          ></permissions>
        </template>
      </sui-segment>
    </sui-form>
  </sui-container>
</template>

<script>
  import axios from 'axios'
  import Permissions from "./components/Permissions";
  export default {
    name: 'app',
    components: {Permissions},
    data() {
      return {
        url: 'https://play.google.com/store/apps/details?id=org.telegram.messenger&hl=en',
        errors: null,
        permissions: null,
        loading: false,
      }
    },
    methods: {
      requestPermission() {
        this.loading = true
        this.errors = null
        this.permissions = null
        axios.post(
          '/permissions', {'url': this.url}
        ).then(response => {
          if (response.status === 200) {
            this.permissions = response.data.permissions
            this.loading = false
          } else if (response.status === 202) {
            setTimeout(this.requestPermission, 300)
          }
        }).catch(error => {
          this.errors = error.response.data.errors
          this.loading = false
        })
      }
    },
  }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
