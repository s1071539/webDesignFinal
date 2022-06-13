<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.title{
    text-align:center; 
    font-size:30px;
}
.caption{
    text-align:left; 
    font-size:20px;
}
.input{
    width:400px;
    border-color:black;
}
.button{
    font-size:30px;
    width:400px;
    background-color:#439EFF;
    color:black;
}
.src{
    border: none;
    color: black;
    background-color: white;
    cursor: pointer;
    text-decoration:underline;
    font-size:20px;
}

</style>

<template>
  <div style="margin-top:-50px">
    <img src="../assets/logo.png">
    <el-card style="margin:100px auto; width:500px; position: relative">
        <div style="position: absolute; right: 0; top: 0;">
            <el-button  icon="el-icon-close" circle  @click="exit"></el-button>
        </div>
        <div style="margin:0 auto; width:400px; font-size:20px">
            <br><br>
            <div class="title">Log in to your account</div><br><br>
            <div class="caption">Account<span style="color:red">*</span></div>
            <el-input class="input" v-model="form.user" placeholder="請輸入帳號(使用者名稱)"></el-input><br><br>
            <div class="caption">Password<span style="color:red">*</span></div>
            <el-input class="input" v-model="form.password" placeholder="請輸入密碼" show-password></el-input><br><br>
            <div class="caption">Email<span style="color:red">*</span></div>
            <el-input class="input" v-model="form.email" placeholder="請輸入信箱"></el-input><br><br><br>
            <el-button class="button"  plain @click="signup">註冊</el-button><br><br>
             
        </div>
    </el-card>
  </div>
</template>

<script>
import * as THREE from 'three'
export default {
  name: 'signup',
  data: function() {
        return { 
            user_data:[],
            form:{
              id:0,
              user:'',
              password:'',
              mypassword:'',
              email:'',
              groups:'',
              region:'',
              myregion:'',
              record:'',
              description:'',
              admin_mail:'',
            },
        }
  },
  created(){
        this.axios.get("/get_all_user",{
        }).then((response)=>{
            this.user_data = response.data;
        });
  },
  mounted() {//監聽enter 若按enter則觸發login
    let _this = this;
    document.onkeydown = function(e) {
        if (_this.$route.name == "signup") {
            let key = window.event.keyCode;
            if (key == 13) 
                _this.signup();
            }
    }
    
  },
  methods:{
    signup(){
        if(this.form.user == ''){
            this.$message({message: '請填入使用者名稱', type: 'error'});
            return;
        }
        if(this.form.password == ''){
            this.$message({message: '請填入使用者密碼', type: 'error'});
            return;
        }
        if(this.form.email == ''){
            this.$message({message: '請填入使用者信箱', type: 'error'});
            return;
        }
        if(this.form.email.split('@')[1] == undefined){
            this.$message({message:'請填入正確email格式', type:'error'});
            return;
        }
        for(let user of this.user_data){
            if(this.form.user == user['user']){
                this.$message({message: '使用者 '+this.form.user+' 已存在!', type: 'error'});
                return;
            }
        }
        
        this.axios.get("/operator_user",{
            params:{
                operator: "add",
                form: JSON.stringify(this.form),
            }
        }).then((response)=>{
            this.$message({message: '帳號建立成功', type: 'success'});
            this.$router.push({name: 'login'});
        })

    },
    exit(){
        this.$router.push({name: 'login'});
    },
  }
}
</script>