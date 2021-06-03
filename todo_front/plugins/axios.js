import { get } from 'lodash'

export default function ({ $axios, store, app, redirect, $auth }) {
  // $axios.onRequest((config) => {})

  $axios.onError((error) => {
    const code = parseInt(error.response && error.response.status)
    if (code === 401) {
      if (get(error, 'response.data.detail', '') === 'Invalid token.') {
        // console.log('invalid token detected, logging out')
        app.$auth.logout()
      }
    }
  })
}
