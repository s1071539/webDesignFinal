<style>
.el-tabs{
    
    position: relative;
    top: 150px;
    width: 80%;
    margin: 0 auto;
}
.add-form-input{
  width:150px;
  left: 0px;
  position: absolute;
}
.el-upload-dragger{
  width: auto;
  height: auto;
}
</style>

<template>
  <div style="margin-top:-50px">
    <div style="position: absolute;top: 20px;left: 100px;">
      <el-button  style="font-size: 30px;" icon="el-icon-back" type="primary" @click="goback"></el-button>
    </div>

    <!-- 新增商品 -->
    <div style="position: absolute;top: 20px;right: 100px;">
      <el-button  style="font-size: 30px;" icon="el-icon-circle-plus" circle type="primary" @click="add_product_lock=true"></el-button>
      <el-dialog title="商品表單-增加" :visible.sync="add_product_lock">
        <el-form :model="add_product_form" label-width="80px" label-position=right>
          <el-form-item  label="商品" ><el-input v-model="add_product_form.name"   class="add-form-input" placeholder="請輸入商品名稱"></el-input></el-form-item>
          <el-form-item  label="價格" ><el-input v-model="add_product_form.price"  class="add-form-input" placeholder="請輸入價格"></el-input></el-form-item>
          <el-form-item  label="數量" ><el-input v-model="add_product_form.amount" class="add-form-input" placeholder="請輸入數量"></el-input></el-form-item>
          <el-form-item  label="種類" >
            <el-select v-model="add_product_form.group" placeholder="請選擇種類" class="add-form-input">
              <el-option label="VT" value="VT"></el-option>
              <el-option label="APEX" value="APEX"></el-option>
              <el-option label="手機" value="手機"></el-option>
              <el-option label="食物" value="食物"></el-option>
              <el-option label="口罩" value="口罩"></el-option>
              <el-option label="娃娃" value="娃娃"></el-option>
              <el-option label="成人" value="成人"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item  label="照片上傳">
            <div style="position:relative; left: -50px;">
              <!--
              <el-upload
                action="111"
                list-type="picture-card"
                :http-request = "customUpload"
                :on-change="file_change"
                accept=".png,.jpg"
                :limit="1"
                drag
                style="width:auto; height:auto;"
              >
                <i slot="default" class="el-icon-plus"></i>
              </el-upload>
              -->
              <input type="file" accept="image/*" @change="readFile">
            </div>
          </el-form-item>
          </el-form>

          <div slot="footer" class="dialog-footer">
            <el-button type="primary" @click="add_product" plain>確定</el-button>
            <el-button type="danger" @click="add_product_lock=false" plain>取消</el-button>
          </div>
          
      </el-dialog>
    </div>

    

    <div>
    <el-tabs type="border-card" >
        <el-tab-pane label="帳號設定">
            <el-table :data="user_data">
                <el-table-column prop="user" label="使用者" ></el-table-column>
                <el-table-column prop="password" label="密碼" ></el-table-column>
                <el-table-column prop="email" label="信箱" ></el-table-column>
                <el-table-column prop="description" label="操作" width="100">
                  <template slot-scope = "{row,$index}" >
                    <el-button type="primary" icon="el-icon-edit" size="small" circle @click="edit_user_dialog(row.user)"></el-button>
                    <el-button v-if="row.user != 'admin' " type="danger" icon="el-icon-delete" size="small" circle @click="delete_user(row)"></el-button>
                      <el-dialog title="使用者表單-修改" :visible.sync="edit_user_lock">
                        <el-form :model="user_form" label-width="80px">
                          <el-form-item prop="user" label="使用者" ><el-input v-model="user_form.user" style="width:200px;"placeholder="請輸入使用者名稱"></el-input></el-form-item>
                          <el-form-item prop="password" label="密碼" ><el-input v-model="user_form.password" style="width:200px;"placeholder="請輸入密碼"></el-input></el-form-item>
                          <el-form-item prop="email" label="信箱" ><el-input v-model="user_form.email" style="width:300px;"placeholder="請輸入信箱"></el-input></el-form-item>
                        </el-form>
                        <div slot="footer" class="dialog-footer">
                          <el-button type="primary" @click="edit_user" plain>確定</el-button>
                          <el-button type="danger" @click="edit_user_lock=false" plain>取消</el-button>
                        </div>
                      </el-dialog>
                  </template>
                </el-table-column>
            </el-table>
        </el-tab-pane>

        <el-tab-pane label="商品管理">
            <el-table :data="product_data"  max-height="700" fit>
              <el-table-column align="center" width="300px">
                <template slot="header" slot-scope="scope">
                  <div>商品</div>
                </template>
                <template slot-scope="scope">
                  <img :src= "scope.row.url" style="max-width: 300px;">
                  <p>{{scope.row.name}}</p>
                </template>
              </el-table-column>

              <el-table-column align="center" label="價格" prop="price" sortable></el-table-column>
              <el-table-column align="center" label="數量" prop="amount" sortable></el-table-column>
              <el-table-column align="center" label="熱門度" prop="hot" sortable></el-table-column>
              <el-table-column align="center" label="上架時間" prop="time" sortable></el-table-column>
              <el-table-column prop="description" label="操作" width="100">
                  <template slot-scope = "{row,$index}" >
                    <el-button type="primary" icon="el-icon-edit" size="small" circle @click="edit_product_dialog(row)"></el-button>
                    <el-button type="danger" icon="el-icon-delete" size="small" circle @click="delete_product(row)"></el-button>
                      <el-dialog title="商品表單-修改" :visible.sync="edit_product_lock">
                        <el-form :model="product_form" label-width="80px">
                          <el-form-item prop="name" label="商品" ><el-input v-model="product_form.name" style="width:200px;"placeholder="請輸入商品名稱"></el-input></el-form-item>
                          <el-form-item prop="price" label="價格" ><el-input v-model="product_form.price" style="width:200px;"placeholder="請輸入價格"></el-input></el-form-item>
                          <el-form-item prop="amount" label="數量" ><el-input v-model="product_form.amount" style="width:300px;"placeholder="請輸入數量"></el-input></el-form-item>
                          <el-form-item prop="hot" label="熱門度" ><el-input v-model="product_form.hot" style="width:300px;"placeholder="請輸入熱門度"></el-input></el-form-item>
                          <el-form-item prop="time" label="上架時間" ><el-input v-model="product_form.time" style="width:300px;"placeholder="請輸入上架時間"></el-input></el-form-item>
                        </el-form>
                        <img :src= "product_form.url" style="position: absolute; right: 50px; top: 50px;">
                    
                        <div slot="footer" class="dialog-footer">
                          <el-button type="primary" @click="edit_product" plain>確定</el-button>
                          <el-button type="danger" @click="edit_product_lock=false" plain>取消</el-button>
                        </div>
                      </el-dialog>
                  </template>
                </el-table-column>
            </el-table>
        </el-tab-pane>
    </el-tabs>
    </div>

  </div>
</template>

<script>


export default {
  name: 'manage',
  data: function() {
        return { 
            user:"",
            user_data:[],
            product_data:[],
            edit_user_lock:false,
            edit_product_lock:false,
            add_product_lock:false,
            user_form:{
              id:0,
              user:'',
              password:'',
              email:'',
            },
            product_form:{
              id:0,
              name:'',
              price:'',
              amount:'',
              hot:'',
              time:'',
              url:'',
            },
            add_product_form:{
              name:'',
              price:'',
              amount:'',
              time:'',
              owner:'',
              group:'',
            },
            add_product_url:'',
            fileList:[],
            
        }
  },
  created(){
    this.user = JSON.parse(sessionStorage.getItem("user"));
    
    this.axios.post("/get_all_user",{
    }).then((response)=>{
      if(this.user != 'admin')
          this.user_data = response.data.filter((item)=>{ return item['user'] == this.user});
      else
          this.user_data = response.data;
    });

    if(sessionStorage["user"] != undefined){
      this.user = JSON.parse(sessionStorage["user"])



      this.axios.get('/get_all_product',{
      params:{
          user: this.user
        }
      }).then(response => {
        this.product_data = response.data
        this.axios.post('/get_all_product_url').then(response => { 
          for (let i in response.data){
            this.product_data[i]['url'] = response.data[i]
          }
          this.product_data = this.product_data.filter((item) => {return item['owner'] == this.user})
          this.table_data = this.product_data
        })
      })

    }
    
  },
  mounted() {
    
    
  },
  methods:{
    goback(){
      this.$router.push({name: 'Show_All'});
    },
    edit_user_dialog(user_name){
        for(let user of this.user_data)
          if(user_name == user['user']){
              this.user_form.id = user['user_id'];
              this.user_form.user = user['user'];
              this.user_form.password = user['password'];
              this.user_form.email = user['email'];
          }
        this.edit_user_lock = true;
    },
    edit_product_dialog(data){
        this.product_form.id = data['id'];
        this.product_form.name = data['name']
        this.product_form.price = data['price']
        this.product_form.amount = data['amount']
        this.product_form.hot = data['hot']
        this.product_form.time = data['time']
        this.product_form.url = data['url']
        this.edit_product_lock = true;
    },
    edit_user(){
      this.axios.get("/operator_user",{
            params:{
                operator: 'modify',
                form: JSON.stringify(this.user_form),
            }
            }).then((response)=>{
                this.user_form.id = 0;
                this.user_form.user = '';
                this.user_form.password = '';
                this.user_form.email = '';
                this.$message({message: '帳號修改成功', type: 'success'});
                location.reload();
            });
    },
    edit_product(){
      this.axios.get("/operator_product",{
            params:{
                operator: 'modify',
                form: JSON.stringify(this.product_form),
            }
            }).then((response)=>{
                this.product_form.id = 0;
                this.product_form.name = '';
                this.product_form.price = '';
                this.product_form.amount = '';
                this.product_form.hot = '';
                this.product_form.time = '';
                this.product_form.url ='';
                this.$message({message: '商品修改成功', type: 'success'});
                location.reload();
            });
    },
    delete_user(row){
      this.$confirm('是否刪除 ' + row['user'] + ' ?', '刪除', {
            confirmButtonText: '確定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
            this.axios.get("/operator_user",{
            params:{
                user_id: row['user_id'],
                operator:'delete'
            }
            }).then((response)=>{
                location.reload();
            });

            this.$message({type: 'success',message: '删除成功!'});

          }).catch(() => {
            this.$message({type: 'info',message: '已取消删除'});          
          });
    },
    delete_product(row){
      this.$confirm('是否刪除 ' + row['name'] + ' ?', '刪除', {
            confirmButtonText: '確定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
            this.axios.get("/operator_product",{
            params:{
                id: row['id'],
                operator:'delete'
            }
            }).then((response)=>{
                location.reload();
            });

            this.$message({type: 'success',message: '删除成功!'});

          }).catch(() => {
            this.$message({type: 'info',message: '已取消删除'});          
          });
    },
    customUpload(file){//此function拿來覆蓋action 使upalod不自動上傳
    },
    file_change(file){
      this.fileList = []
      this.fileList.push(file);
    },
    add_product(){
      if(this.add_product_form.name == ""){
        this.$message({type: 'warning',message: '請輸入商品名稱'});
        return;
      }
      if(this.add_product_form.price == ""){
        this.$message({type: 'warning',message: '請輸入價格'});  
        return;
      }
      if(this.add_product_form.amount == ""){
        this.$message({type: 'warning',message: '請輸入數量'});  
        return;
      }
      if(this.add_product_form.group == ""){
        this.$message({type: 'warning',message: '請輸入種類'});  
        return;
      }

      var today=new Date();
      var currentDateTime =today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
      this.add_product_form.time = currentDateTime;
      this.add_product_form.owner = this.user;
      this.axios.get("/operator_product",{
        params:{
            operator: 'add',
            form: JSON.stringify(this.add_product_form),
        }
      }).then((response)=>{
          let new_id = response.data
          this.axios.post('/add_product_url', {
            new_id:  new_id,
            url: JSON.stringify(this.add_product_url)
          }).then(response => { 
            this.add_product_form.name = '';
            this.add_product_form.price = '';
            this.add_product_form.amount = '';
            this.add_product_form.time = '';
            this.add_product_form.owner = '';
            this.add_product_form.group ='';
            this.add_product_url ='';
            location.reload();
          });
        });
    },
  
    readFile(e) {
      if (e.srcElement.files && e.srcElement.files[0]) {
        var FR= new FileReader();
        var that = this
        FR.addEventListener("load", function(e) {
          that.add_product_url = e.target.result;
        });
        FR.readAsDataURL( e.srcElement.files[0] );
      }
      
    }


  }
}
</script>