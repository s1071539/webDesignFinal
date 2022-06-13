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
            <div class="title">Find your account</div><br><br>
            <div class="caption">Account<span style="color:red">*</span></div>
            <el-input class="input" v-model="user" placeholder="請輸入帳號(使用者名稱)"></el-input><br><br>
            <div class="caption">Email<span style="color:red">*</span></div>
            <el-input class="input" v-model="email" placeholder="請輸入信箱"></el-input><br><br><br>
            <el-button class="button"  plain @click="reset_password">找尋</el-button><br><br>
             
        </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'resetPassword',
  data: function() {
        return { 
            user_data:{},
            user:'',
            email: '',
            password: '',
        }
  },
  created(){
    this.axios.post("/get_all_user",{
    }).then((response)=>{
          response.data.forEach((item)=>{
              this.user_data[item['user']] = item['email']
              
          })
    });
  },
  mounted() {//監聽enter 若按enter則觸發login
    let _this = this;
    document.onkeydown = function(e) {
        if (_this.$route.name == "resetPassword") {
            let key = window.event.keyCode;
            if (key == 13) 
                _this.reset_password();
            }
    }
    
  },
  methods:{
    reset_password(){
        if(this.user == ''){
            this.$message({message: '請填入使用者名稱', type: 'error'});
            return;
        }
        if(this.email == ''){
            this.$message({message: '請填入使用者信箱', type: 'error'});
            return;
        }
        if(this.email.split('@')[1] == undefined){
            this.$message({message:'請填入正確email格式', type:'error'});
            return;
        }
        for(let user of this.user_data){
            if(this.user_data[this.user] == undefined){
                this.$alert('使用者不存在')
                return
            }
            if(this.user_data[this.user] != this.email){
                this.$alert('信箱錯誤')
                return
            }
            
            this.$prompt('請輸入新密碼', '新密碼', {
                confirmButtonText: '確定',
                cancelButtonText: '取消',
                inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*/,
                inputErrorMessage: '只接受英文和數字'
                }).then(({ value }) => { 
                    this.$message({type: 'success',message: '已重設密碼，請使用新密碼登入'});
                }).catch(() => { 
                    this.$message({type: 'info',message: '取消输入'}
                );       
            });
            
        }
        

    },
    exit(){
        this.$router.push({name: 'login'});
    },
  }
}
</script>