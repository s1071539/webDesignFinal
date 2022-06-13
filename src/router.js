import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/login'
import Signup from '@/components/signup'
import ResetPassword from '@/components/resetPassword'
import Show_All from '@/components/Show_All'
import Play from '@/components/play'
import Manage from '@/components/manage'

Vue.use(Router)

export default new Router({
  routes: [
    {//防止有人亂try結構
      path: '*',
      redirect: '/',
    },
    {
      path: '/',
      name: 'Show_All',
      component: Show_All
    },
    {
      path: '/Show_All',
      name: 'Show_All',
      component: Show_All
    },
    {
      path: '/play',
      name: 'play',
      component: Play
    },
    {
      path: '/signup',
      name: 'signup',
      component: Signup
    },
    {
      path: '/resetPassword',
      name: 'resetPassword',
      component: ResetPassword
    },
    {
      path: '/manage',
      name: 'manage',
      component: Manage
    },
  ]
})
