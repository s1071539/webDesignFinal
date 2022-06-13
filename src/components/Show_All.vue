<style scoped>
.memeber_button {
  position: relative;
  top: 50px;
  right: -700px;
}
.search_div {
  width: 40%;
  margin: 0 auto;
  display: flex;
  position: absolute;
  top: 70px;
  left: 800px;
}
.tabs_div {
  position: relative;
  left: 60px;
  top: 60px;
}

.manage_button {
  text-align: center;
  vertical-align: middle;
  margin-top: 5px;
}
</style>


<template>
  <div>
    <el-dialog
      title="期末專題說明"
      :visible.sync="helloDialogVisible"
      width="50%"
      @close="helloDialogClose"
    >
      <div style="text-align: initial; margin: auto; width: 80%">
      <span style="font-size: 21px; line-height: 70px">
        學號: 1071539 姓名: 黃俊凱 <br />
        本專案結合 Vue.js + Django + PostgreSQL 並放置於Heroku<br />
        主要功能是打造一個虛擬夾娃娃機<br />
        並且使用到製作期中時所使用到的Three.js作為3D模型<br />
        此外為了實現物理碰撞，加上Cannon.js作為簡易的物理引擎<br />
        原始碼可以在<el-link
          href="https://github.com/s1071539/webDesignFinal"
          type="primary"
          style="font-size: 21px"
          >GitHub</el-link
        >上查看<br />
        ● 點擊圖片可進入遊戲<br />
        ● 點擊右上+按鈕可新增商品<br />
      </span>
      
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="helloDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="helloDialogVisible = false"
          >确 定</el-button
        >
      </span>
    </el-dialog>

    <!-- all page -->
    <el-carousel
      height="65px"
      style="
        width: 30%;
        border: 7px solid;
        border-color: antiquewhite;
        border-radius: 40px;
        margin-left: 30px;
        background: cornsilk;
      "
    >
      <el-carousel-item
        v-for="item in ['1071539 黃俊凱', '網站設計期末專題', '線上夾娃娃']"
        :key="item"
      >
        <h3 class="small">{{ item }}</h3>
      </el-carousel-item>
    </el-carousel>
    <span style="position: absolute; top: 30px; right: 200px"
      ><i class="el-icon-coin"></i>目前餘額：{{ user_money }}$</span
    >
    <el-popover
      placement="bottom"
      trigger="click"
      width="300"
      title="選取儲值金額"
      ref="money_pop"
    >
      <br />
      <el-form :model="recharge" label-width="80px">
        <div style="left: 20px; position: relative">
          <el-row>
            <el-col :span="7"
              ><el-radio v-model="recharge.money" label="50" border
                >50</el-radio
              ></el-col
            >
            <el-col :span="7"
              ><el-radio v-model="recharge.money" label="100" border
                >100</el-radio
              ></el-col
            >
            <el-col :span="7"
              ><el-radio v-model="recharge.money" label="200" border
                >200</el-radio
              ></el-col
            >
          </el-row>
          <el-row>
            <el-col :span="7" style="margin-top: 10px"
              ><el-radio v-model="recharge.money" label="500" border
                >500</el-radio
              ></el-col
            >
            <el-col :span="7" style="margin-top: 10px"
              ><el-radio v-model="recharge.money" label="750" border
                >750</el-radio
              ></el-col
            >
            <el-col :span="7" style="margin-top: 10px"
              ><el-radio v-model="recharge.money" label="1000" border
                >1000</el-radio
              ></el-col
            >
          </el-row>
        </div>
        <div style="text-align: right; margin-top: 20px">
          <el-button
            size="mini"
            type="text"
            @click="$refs['money_pop'].doClose()"
            >取消</el-button
          >
          <el-button type="primary" size="mini" @click="set_user_money"
            >确定</el-button
          >
        </div>
      </el-form>
      <el-link
        type="primary"
        slot="reference"
        style="position: absolute; top: 30px; right: 100px"
        >儲值<i class="el-icon-circle-plus"></i
      ></el-link>
    </el-popover>

    <div class="search_div">
      <!-- search -->
      <el-input
        style="width: 300px"
        v-model="search_text"
        placeholder="请输入内容"
      ></el-input>
      <el-button
        type="primary"
        icon="el-icon-search"
        circle
        @click="search"
      ></el-button>
    </div>

    <!-- 新增商品 -->
    <div style="position: absolute; top: 70px; right: 100px">
      <el-button
        style="font-size: 30px"
        icon="el-icon-circle-plus"
        circle
        type="primary"
        @click="add_product_lock = true"
      ></el-button>
      <el-dialog title="商品表單-增加" :visible.sync="add_product_lock">
        <el-form
          :model="add_product_form"
          label-width="80px"
          label-position="right"
        >
          <el-form-item label="商品"
            ><el-input
              v-model="add_product_form.name"
              class="add-form-input"
              placeholder="請輸入商品名稱"
            ></el-input
          ></el-form-item>
          <el-form-item label="價格"
            ><el-input
              v-model="add_product_form.price"
              class="add-form-input"
              placeholder="請輸入價格"
            ></el-input
          ></el-form-item>
          <el-form-item label="數量"
            ><el-input
              v-model="add_product_form.amount"
              class="add-form-input"
              placeholder="請輸入數量"
            ></el-input
          ></el-form-item>
          <el-form-item label="種類">
            <el-select
              v-model="add_product_form.group"
              placeholder="請選擇種類"
              class="add-form-input"
            >
              <el-option label="VT" value="VT"></el-option>
              <el-option label="APEX" value="APEX"></el-option>
              <el-option label="手機" value="手機"></el-option>
              <el-option label="食物" value="食物"></el-option>
              <el-option label="口罩" value="口罩"></el-option>
              <el-option label="娃娃" value="娃娃"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="照片上傳">
            <div style="position: relative; left: -50px">
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
              <input type="file" accept="image/*" @change="readFile" />
            </div>
          </el-form-item>
        </el-form>

        <div slot="footer" class="dialog-footer">
          <el-button type="primary" @click="add_product" plain>確定</el-button>
          <el-button type="danger" @click="add_product_lock = false" plain
            >取消</el-button
          >
        </div>
      </el-dialog>
    </div>

    <div style="display: flex; margin-left: 50px; margin-top: 20px">
      <div style="width: 170px">
        <!-- 分類表 -->
        <el-menu
          default-active="全部"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          @select="select_menu"
        >
          <el-menu-item index="全部">
            <i class="el-icon-position"></i> <span slot="title">全部</span>
          </el-menu-item>
          <el-menu-item index="VT">
            <i class="el-icon-position"></i> <span slot="title">VT</span>
          </el-menu-item>
          <el-menu-item index="APEX">
            <i class="el-icon-position"></i> <span slot="title">APEX</span>
          </el-menu-item>
          <el-menu-item index="手機">
            <i class="el-icon-position"></i> <span slot="title">手機</span>
          </el-menu-item>
          <el-menu-item index="食物">
            <i class="el-icon-position"></i> <span slot="title">食物</span>
          </el-menu-item>
          <el-menu-item index="口罩">
            <i class="el-icon-position"></i> <span slot="title">口罩</span>
          </el-menu-item>
          <el-menu-item index="娃娃">
            <i class="el-icon-position"></i> <span slot="title">娃娃</span>
          </el-menu-item>
        </el-menu>
      </div>

      <div style="width: 100%">
        <div style="width: 90%; margin: auto auto">
          <!-- 商品 -->
          <el-table :data="table_data" max-height="700" fit>
            <el-table-column align="center" width="300px">
              <template slot="header" slot-scope="scope">
                <div>商品名稱</div>
              </template>

              <template slot-scope="scope">
                <img
                  :src="scope.row.url"
                  style="cursor: pointer; max-width: 300px"
                  @click="cell_click(scope.row)"
                />

                <p>{{ scope.row.name }}</p>
              </template>
            </el-table-column>
            <el-table-column align="center" label="價格" prop="price" sortable>
            </el-table-column>
            <el-table-column align="center" label="數量" prop="amount" sortable>
            </el-table-column>
            <el-table-column align="center" label="熱門度" prop="hot" sortable>
            </el-table-column>
            <el-table-column
              align="center"
              label="上架時間"
              prop="time"
              sortable
            >
            </el-table-column>
          </el-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Show_All",
  data() {
    return {
      user: "",
      user_money: "",
      search_text: "",
      product_data: [],
      table_data: [],
      recharge: {
        number: "",
        digtal3: "",
        money: "",
      },
      activeName: "商品",
      edit_user_lock: false,
      edit_product_lock: false,
      add_product_lock: false,
      user_form: {
        id: 0,
        user: "",
        password: "",
        email: "",
      },
      product_form: {
        id: 0,
        name: "",
        price: "",
        amount: "",
        hot: "",
        time: "",
        url: "",
      },
      add_product_form: {
        name: "",
        price: "",
        amount: "",
        time: "",
        owner: "",
        group: "",
      },
      add_product_url: "",
      fileList: [],
      helloDialogVisible: true,
      tips: [true, false, false, false, false, false, false, false, false],
    };
  },
  created() {
    sessionStorage.setItem("user", JSON.stringify("admin"));
    sessionStorage.setItem("token", "ImLogin");

    if (sessionStorage["user"] != undefined) {
      this.user = JSON.parse(sessionStorage["user"]);

      this.axios
        .get("/get_all_product", {
          params: {
            user: this.user,
          },
        })
        .then((response) => {
          this.product_data = response.data;
          this.axios.post("/get_all_product_url").then((response) => {
            for (let i in response.data) {
              this.product_data[i]["url"] = response.data[i];
            }
            this.table_data = this.product_data;
          });
        });

      this.axios.post("/get_all_user", {}).then((response) => {
        let db_user = response.data.filter((item) => {
          return item["user"] == this.user;
        });
        this.user_money = db_user[0]["setting"];
      });
    }
  },
  watch: {},
  methods: {
    helloDialogClose() {
      this.tips[0] = true;
      console.log(this.tips);
    },
    manage() {
      this.$router.push({ name: "manage" });
    },
    logout() {
      sessionStorage.clear();
      this.$router.push("/login");
    },
    select_menu(index) {
      switch (index) {
        case "全部":
          this.table_data = this.product_data;
          break;
        case "VT":
          this.table_data = this.product_data.filter((item) => {
            return item["group"] == "VT";
          });
          break;
        case "APEX":
          this.table_data = this.product_data.filter((item) => {
            return item["group"] == "APEX";
          });
          break;
        case "手機":
          this.table_data = this.product_data.filter((item) => {
            return item["group"] == "手機";
          });
          break;
        case "食物":
          this.table_data = this.product_data.filter((item) => {
            return item["group"] == "食物";
          });
          break;
        case "口罩":
          this.table_data = this.product_data.filter((item) => {
            return item["group"] == "口罩";
          });
          break;
        case "娃娃":
          this.table_data = this.product_data.filter((item) => {
            return item["group"] == "娃娃";
          });
          break;
      }
    },
    cell_click(row) {
      sessionStorage.setItem("play_info", JSON.stringify(row));
      this.$router.push({ name: "play" });
    },
    search() {
      this.table_data = this.product_data.filter((item) => {
        return item["name"].includes(this.search_text);
      });
    },
    set_user_money() {
      this.axios
        .post("/set_user_money", {
          user: this.user,
          money: this.recharge.money,
        })
        .then((response) => {
          location.reload();
        });
    },

    customUpload(file) {
      //此function拿來覆蓋action 使upalod不自動上傳
    },
    file_change(file) {
      this.fileList = [];
      this.fileList.push(file);
    },
    add_product() {
      if (this.add_product_form.name == "") {
        this.$message({ type: "warning", message: "請輸入商品名稱" });
        return;
      }
      if (this.add_product_form.price == "") {
        this.$message({ type: "warning", message: "請輸入價格" });
        return;
      }
      if (this.add_product_form.amount == "") {
        this.$message({ type: "warning", message: "請輸入數量" });
        return;
      }
      if (this.add_product_form.group == "") {
        this.$message({ type: "warning", message: "請輸入種類" });
        return;
      }

      var today = new Date();
      var currentDateTime =
        today.getFullYear() +
        "-" +
        (today.getMonth() + 1) +
        "-" +
        today.getDate();
      this.add_product_form.time = currentDateTime;
      this.add_product_form.owner = this.user;
      this.axios
        .get("/operator_product", {
          params: {
            operator: "add",
            form: JSON.stringify(this.add_product_form),
          },
        })
        .then((response) => {
          let new_id = response.data;
          this.axios
            .post("/add_product_url", {
              new_id: new_id,
              url: JSON.stringify(this.add_product_url),
            })
            .then((response) => {
              this.add_product_form.name = "";
              this.add_product_form.price = "";
              this.add_product_form.amount = "";
              this.add_product_form.time = "";
              this.add_product_form.owner = "";
              this.add_product_form.group = "";
              this.add_product_url = "";
              location.reload();
            });
        });
    },

    readFile(e) {
      if (e.srcElement.files && e.srcElement.files[0]) {
        var FR = new FileReader();
        var that = this;
        FR.addEventListener("load", function (e) {
          that.add_product_url = e.target.result;
        });
        FR.readAsDataURL(e.srcElement.files[0]);
      }
    },
  },
};
</script>
