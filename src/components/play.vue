<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.title {
  text-align: center;
  font-size: 30px;
}
.caption {
  text-align: left;
  font-size: 20px;
}
.input {
  width: 400px;
  border-color: black;
}
.button {
  font-size: 30px;
  width: 400px;
  background-color: #439eff;
  color: black;
}

.btn {
  font-size: 22px;
  position: relative;
  display: inline-block;
  background: #222;
  background: linear-gradient(
    45deg,
    rgba(34, 34, 34, 1),
    rgba(34, 34, 34, 1),
    rgba(34, 34, 34, 1)
  );
  color: #fff;
  font-size: 14px;
  font-family: "Josefin Sans", sans-serif;
  font-weight: bold;
  line-height: 1;
  text-align: center;
  text-indent: 0.15em;
  letter-spacing: 0.15em;
  box-sizing: border-box;
  box-shadow: 0px 10px 15px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

.btn {
  background: linear-gradient(
    45deg,
    rgba(0, 0, 255, 0.9),
    rgba(255, 255, 0, 0.9),
    rgba(255, 0, 0, 0.9)
  );
  background: -webkit-linear-gradient(
    45deg,
    rgba(0, 0, 255, 0.9),
    rgba(255, 255, 0, 0.9),
    rgba(255, 0, 0, 0.9)
  );
  background-size: 600% 600%;
  animation: AnimeGrade 10s ease infinite;
  text-decoration: none;
  letter-spacing: 0.28em;
  box-shadow: 0px 10px 20px 0px rgba(0, 0, 0, 0.3);
}

@keyframes AnimeGrade {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
</style>

<template>
  <div>
    <div style="position: absolute; top: 20px; left: 100px">
      <el-button
        style="font-size: 30px"
        icon="el-icon-back"
        type="primary"
        @click="goback"
      ></el-button>
      <div style="margin-top:50px; border:dotted; font-size: 20px">
        <oi>
          <br /><br /><br /><br />
          <li style="padding: 0px 25px">上下左右鍵操控爪子</li>
          <br /><br /><br />
          <li>滑鼠拖曳、滾輪操控視角</li>
          <br /><br /><br />
          <li>按空白鍵抓取物品</li>
          <br /><br /><br />
          <li>↓按下開始遊戲按鈕↓</li>
          <br /><br /><br />
          <div>
            <el-button
              @click="start_game"
              v-show="play_lock"
              class="btn"
              style="font-size: 22px"
              >開始遊戲</el-button
            >
          </div>
          <br /><br />
        </oi>
      </div>
    </div>

    <span style="position: absolute; top: 30px; right: 200px"
      ><i class="el-icon-coin"></i>目前餘額：{{ user_money }}$</span
    >
    <el-popover
      placement="bottom"
      trigger="click"
      width="300"
      title="信用卡儲值"
      ref="money_pop"
    >
      <br />
      <el-form :model="recharge" label-width="80px">
        <el-form-item prop="number" label="卡號">
          <el-input
            v-model="recharge.number"
            style="width: 200px; display: block"
            placeholder="請輸入卡號"
            type="text"
          >
            <i class="el-icon-bank-card" slot="prefix"></i>
          </el-input>
        </el-form-item>
        <el-form-item prop="digtal3" label="後三碼">
          <el-input
            v-model="recharge.digtal3"
            style="width: 200px; display: block"
            placeholder="請輸入後三碼"
          ></el-input>
        </el-form-item>
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

    <div style="position: absolute; top: 120px; right: 100px">
      <el-button
        style="font-size: 30px"
        icon="el-icon-s-cooperation"
        type="primary"
        @click="open_prize_form"
      ></el-button>
      <el-dialog title="已獲得獎品" :visible.sync="prize_form" width='700px'>
        <div style="display: flex">
          <div style="width: 100%">
            <div
              v-for="(item, index) in product_url"
              style="float: left; margin-top: 20px"
            >
              <div>
                <img :src="item" style="width: 150px; height: 150px" />
              </div>
              <div>
                <el-checkbox v-model="prize_selection[index]" label="">{{
                  index
                }}</el-checkbox>
              </div>
            </div>
          </div>
        </div>
        <div slot="footer" class="dialog-footer">
          <el-button type="warning" @click="del_prize" plain>丟棄</el-button>
          <el-button type="primary" @click="prize_form = false" plain
            >確定</el-button
          >
        </div>
      </el-dialog>
    </div>

    <canvas id="mainCanvas"></canvas>
    <canvas style="margin: 55px" id="three"></canvas>
  </div>
</template>


<script>
import * as THREE from "three";
import * as CANNON from "cannon";
import * as TControls from "three-trackballcontrols-ts";

export default {
  name: "play",
  data: function () {
    return {
      user: "",
      play_info: [],
      prize_info: [],
      prize_form: false,
      form: {
        name: "",
        cellphone: "",
        adddress: "",
      },
      prize_selection: [],
      index_url_map: [],
      product_url: [],
      user_money: "",
      recharge: {
        number: "",
        digtal3: "",
        money: "",
      },
      play_lock: true,
    };
  },
  created() {
    this.user = JSON.parse(sessionStorage["user"]);
    this.play_info = JSON.parse(sessionStorage["play_info"]);

    this.axios
      .post("/get_user_prize", {
        user: this.user,
      })
      .then((response) => {
        if (response.data != "") this.prize_info = JSON.parse(response.data);
        else this.prize_info = [];
        this.axios.post("/get_all_product_url").then((response) => {
          for (let i in response.data) {
            this.index_url_map[i] = response.data[i];
          }
        });
      });

    this.axios.post("/get_all_user", {}).then((response) => {
      let db_user = response.data.filter((item) => {
        return item["user"] == this.user;
      });
      this.user_money = db_user[0]["setting"];
    });
  },
  mounted() {
    this.initThree();
  },
  methods: {
    open_prize_form() {
      this.axios
        .post("/get_user_prize", {
          user: this.user,
        })
        .then((response) => {
          if (response.data != "") this.prize_info = JSON.parse(response.data);
          else this.prize_info = [];

          this.product_url = [];

          for (let i of this.prize_info) {
            this.product_url.push(this.index_url_map[i - 1]);
          }

          for (let i in this.product_url) {
            this.prize_selection[i] = false;
          }
          this.prize_form = true;
        });
    },
    start_game() {
      if (this.user_money <= 0) {
        this.$message.error("金額不夠，請加值");
        return;
      }
      this.user_money -= 10;
      this.axios.post("/set_user_money", { user: this.user, money: -10 });
      this.play_lock = false;
    },
    set_user_money() {
      this.axios
        .post("/set_user_money", {
          user: this.user,
          money: this.recharge.money,
        })
        .then((response) => {
          location.reload();
          this.$message("加值成功");
        });
    },
    goback() {
      this.$router.push({ name: "Show_All" });
    },
    del_prize() {
      this.axios
        .post("/del_user_prize", {
          user: this.user,
          prize_info: this.prize_selection,
        })
        .then((response) => {
          this.$message("刪除成功");
          location.reload();
        });
    },
    send_prize() {
      if (this.form.name == "") {
        this.$message({ message: "請填寫名字!", type: "error" });
        return;
      }
      if (this.form.cellphone == "") {
        this.$message({ message: "請填寫聯絡方式!", type: "error" });
        return;
      }
      if (this.form.adddress == "") {
        this.$message({ message: "請填寫收貨地址!", type: "error" });
        return;
      }
      this.$message({ message: "已送出!", type: "success" });
      this.form.name = "";
      this.form.cellphone = "";
      this.form.adddress = "";
      location.reload();
    },
    initThree() {
      const canvas = document.querySelector("#three");
      var that = this;
      var controls;
      var light, light2, light3;
      var camera, scene, renderer;
      var body, body2, body3;
      var joystickHead, joystickBody;
      var coin;
      var mySystem, clawSystem, joystickSystem;
      var clawline, clawbody;
      var cameraPositionX, cameraPositionY, cameraPositionZ;
      var up = false,
        right = false,
        down = false,
        left = false;
      var clawlock = false;
      var currentY = 0;
      var clawdown = false;
      var clawup = false;
      var close = false;
      var backOrigin = false;
      var clawMesh1, clawMesh2;
      var new_play_lock = true,
        old_play_lock = true;
      var bingo = undefined;

      let world;
      let sphere, sphere2;
      let friction = 0.5;
      let restitution = 0.7;

      camera = new THREE.PerspectiveCamera(
        45,
        window.innerWidth / window.innerHeight,
        10,
        5000
      );
      camera.position.y = 200;
      camera.position.z = 850;
      cameraPositionX = camera.position.x;
      cameraPositionY = camera.position.y;
      cameraPositionZ = camera.position.z;
      scene = new THREE.Scene();
      scene.background = new THREE.Color("#eee");

      /*mySystem*/
      mySystem = new THREE.Object3D();
      scene.add(mySystem);

      /*light*/
      light = new THREE.DirectionalLight(0xffffff);
      light.position.set(100, 200, 400);
      scene.add(light);
      light2 = new THREE.DirectionalLight(0xffffff);
      light2.position.set(-400, 200, -400);
      scene.add(light2);
      light3 = new THREE.DirectionalLight(0xffffff);
      light3.position.set(100, -400, -400);
      scene.add(light3);

      //背景
      const bggeometry = new THREE.PlaneGeometry(4300, 2500);
      const bgTexture = new THREE.TextureLoader().load(
        require("@/assets/bg.jpg")
      );
      const bgmaterial = new THREE.MeshBasicMaterial({
        map: bgTexture,
        side: THREE.DoubleSide,
      });
      const bgplane = new THREE.Mesh(bggeometry, bgmaterial);
      bgplane.position.z = -2150;
      bgplane.rotation.x = (180 * Math.PI) / 180;
      bgplane.rotation.z = (180 * Math.PI) / 180;
      scene.add(bgplane);

      const bgplane3 = new THREE.Mesh(bggeometry, bgmaterial);
      bgplane3.position.z = 2150;
      bgplane3.rotation.x = (180 * Math.PI) / 180;
      bgplane3.rotation.z = (180 * Math.PI) / 180;
      scene.add(bgplane3);

      const bgplane2 = new THREE.Mesh(bggeometry, bgmaterial);
      bgplane2.position.x = -2150;
      bgplane2.rotation.x = (180 * Math.PI) / 180;
      bgplane2.rotation.y = (270 * Math.PI) / 180;
      bgplane2.rotation.z = (180 * Math.PI) / 180;
      scene.add(bgplane2);

      const bgplane4 = new THREE.Mesh(bggeometry, bgmaterial);
      bgplane4.position.x = 2150;
      bgplane4.rotation.x = (180 * Math.PI) / 180;
      bgplane4.rotation.y = (270 * Math.PI) / 180;
      bgplane4.rotation.z = (180 * Math.PI) / 180;
      scene.add(bgplane4);

      const bggeometry5 = new THREE.PlaneGeometry(4300, 4300);
      const bgTexture5 = new THREE.TextureLoader().load(
        require("@/assets/ground.jpg")
      );
      const bgmaterial5 = new THREE.MeshBasicMaterial({
        map: bgTexture5,
        side: THREE.DoubleSide,
      });
      const bgplane5 = new THREE.Mesh(bggeometry5, bgmaterial5);
      bgplane5.position.y = -1250;
      bgplane5.rotation.x = (270 * Math.PI) / 180;
      scene.add(bgplane5);

      const bggeometry6 = new THREE.PlaneGeometry(4300, 4300);
      const bgTexture6 = new THREE.TextureLoader().load(
        require("@/assets/ground.jpg")
      );
      const bgmaterial6 = new THREE.MeshBasicMaterial({
        map: bgTexture6,
        side: THREE.DoubleSide,
      });
      const bgplane6 = new THREE.Mesh(bggeometry6, bgmaterial6);
      bgplane6.position.y = 1250;
      bgplane6.rotation.x = (270 * Math.PI) / 180;
      scene.add(bgplane6);

      /*玻璃*/
      //下
      var geometry = new THREE.PlaneGeometry(300, 300);
      var material = new THREE.MeshPhongMaterial({
        transparent: true,
        opacity: 0.4,
        side: THREE.DoubleSide,
      });
      var plane = new THREE.Mesh(geometry, material);
      plane.rotation.x = (-90 * Math.PI) / 180;
      scene.add(plane);

      //上
      var geometry = new THREE.PlaneGeometry(300, 300);
      var material = new THREE.MeshPhongMaterial({
        transparent: true,
        opacity: 0.4,
        side: THREE.DoubleSide,
      });
      var plane = new THREE.Mesh(geometry, material);
      plane.rotation.x = (-90 * Math.PI) / 180;
      plane.position.y += 300;
      scene.add(plane);

      //左
      var geometry = new THREE.PlaneGeometry(300, 300);
      var material = new THREE.MeshPhongMaterial({
        transparent: true,
        opacity: 0.4,
        side: THREE.DoubleSide,
      });
      var plane = new THREE.Mesh(geometry, material);
      plane.rotation.y = (-90 * Math.PI) / 180;
      plane.position.x -= 150;
      plane.position.y += 150;
      scene.add(plane);

      //右
      var geometry = new THREE.PlaneGeometry(300, 300);
      var material = new THREE.MeshPhongMaterial({
        transparent: true,
        opacity: 0.4,
        side: THREE.DoubleSide,
      });
      var plane = new THREE.Mesh(geometry, material);
      plane.rotation.y = (90 * Math.PI) / 180;
      plane.position.x += 150;
      plane.position.y += 150;
      scene.add(plane);

      //前
      var geometry = new THREE.PlaneGeometry(300, 300);
      var material = new THREE.MeshPhongMaterial({
        transparent: true,
        opacity: 0.4,
        side: THREE.DoubleSide,
      });
      var plane = new THREE.Mesh(geometry, material);
      plane.position.y += 150;
      plane.position.z += 150;
      scene.add(plane);

      //後
      var geometry = new THREE.PlaneGeometry(300, 300);
      var material = new THREE.MeshPhongMaterial({
        transparent: true,
        opacity: 0.4,
        side: THREE.DoubleSide,
      });
      var plane = new THREE.Mesh(geometry, material);
      plane.position.y += 150;
      plane.position.z -= 150;
      scene.add(plane);

      /*箱子*/
      var texture = new THREE.TextureLoader().load(
        require("@/assets/crate.gif")
      );
      var geometry = new THREE.BoxGeometry(300, 150, 400);
      var material = new THREE.MeshBasicMaterial({ map: texture });
      var cube = new THREE.Mesh(geometry, material);
      cube.position.y -= 80;
      cube.position.z += 50;
      scene.add(cube);
      /* 投幣孔 */
      const coinholeGeometry = new THREE.PlaneGeometry(35, 50, 30, 30);
      const coinholeTexture = new THREE.TextureLoader().load(
        require("@/assets/coin_hole2.png")
      );
      const coinholeMaterial = new THREE.MeshBasicMaterial({
        map: coinholeTexture,
        side: THREE.DoubleSide,
      });
      const coinhole = new THREE.Mesh(coinholeGeometry, coinholeMaterial);
      coinhole.position.x += 94;
      coinhole.position.y -= 80;
      coinhole.position.z += 251;
      scene.add(coinhole);

      /*金幣*/
      const coinGeometry = new THREE.CircleGeometry(12, 32);
      const coinTexture = new THREE.TextureLoader().load(
        require("@/assets/coin.png")
      );
      const coinMaterial = new THREE.MeshBasicMaterial({
        map: coinTexture,
        side: THREE.DoubleSide,
      });
      coin = new THREE.Mesh(coinGeometry, coinMaterial);
      coin.rotation.y = (90 * Math.PI) / 180;
      coin.position.y -= 30;
      scene.add(coin);

      /*控制桿*/
      joystickSystem = new THREE.Object3D();
      scene.add(joystickSystem);

      var joystickHeadgeometry = new THREE.SphereGeometry(10, 32, 32);
      var joystickHeadTexture = new THREE.TextureLoader().load(
        require("@/assets/UV_Grid_Sm.jpg")
      );
      var joystickHeadMaterial = new THREE.MeshPhongMaterial({
        map: joystickHeadTexture,
      });
      joystickHead = new THREE.Mesh(joystickHeadgeometry, joystickHeadMaterial);
      joystickHead.position.y += 20;

      joystickSystem.add(joystickHead);

      var joystickBodygeometry = new THREE.CylinderGeometry(2, 2, 30, 32);
      var joystickBodyTexture = new THREE.TextureLoader().load(
        require("@/assets/UV_Grid_Sm.jpg")
      );
      var joystickBodymaterial = new THREE.MeshBasicMaterial({
        map: joystickBodyTexture,
      });
      joystickBody = new THREE.Mesh(joystickBodygeometry, joystickBodymaterial);
      joystickBody.position.y += 10;
      joystickSystem.add(joystickBody);
      joystickSystem.position.z += 210;

      /*mySystem*/
      mySystem = new THREE.Object3D();
      scene.add(mySystem);

      /*爪子*/
      clawSystem = new THREE.Object3D();
      scene.add(clawSystem);

      var linegeometry = new THREE.CylinderGeometry(0.1, 0.1, 20, 32);
      var linematerial = new THREE.MeshBasicMaterial({ color: 0xffff00 });
      clawline = new THREE.Mesh(linegeometry, linematerial);
      clawSystem.add(clawline);

      class CustomSinCurve extends THREE.Curve {
        constructor(scale = 1) {
          super();
          this.scale = scale;
        }

        getPoint(t, optionalTarget = new THREE.Vector3()) {
          const tx = t * 3 - 1.5;
          const ty = Math.sin(2 * Math.PI * t * 0.6);
          const tz = 0;
          return optionalTarget.set(tx, ty, tz).multiplyScalar(this.scale);
        }
      }

      var path = new CustomSinCurve(20);
      var clawGeometry = new THREE.TubeGeometry(path, 100, 2, 20, false);
      var clawTexture = new THREE.TextureLoader().load(
        require("@/assets/UV_Grid_Sm.jpg")
      );
      var clawMaterial = new THREE.MeshBasicMaterial({ map: clawTexture });
      clawMesh1 = new THREE.Mesh(clawGeometry, clawMaterial);
      clawMesh1.position.x -= 40;
      clawMesh1.position.y += 150;
      clawMesh1.rotation.z = (90 * Math.PI) / 180;
      clawSystem.add(clawMesh1);

      clawMesh2 = new THREE.Mesh(clawGeometry, clawMaterial);
      clawMesh2.position.x += 40;
      clawMesh2.position.y += 150;
      clawMesh2.rotation.z = (90 * Math.PI) / 180;
      clawMesh2.rotation.y = (180 * Math.PI) / 180;
      clawSystem.add(clawMesh2);

      var controlGeometry = new THREE.SphereGeometry(50, 32, 32);
      var controlTexture = new THREE.TextureLoader().load(
        require("@/assets/UV_Grid_Sm.jpg")
      );
      var controlMaterial = new THREE.MeshPhongMaterial({
        map: controlTexture,
      });
      clawbody = new THREE.Mesh(controlGeometry, controlMaterial);
      clawbody.position.y += 200;
      clawbody.scale.y -= 0.1;
      clawSystem.add(clawbody);
      clawSystem.position.y += 50;

      /*line*/
      var linegeometry = new THREE.CylinderGeometry(5, 5, 20, 32);
      var lineTexture = new THREE.TextureLoader().load(
        require("@/assets/UV_Grid_Sm.jpg")
      );
      var linematerial = new THREE.MeshBasicMaterial({ map: lineTexture });
      clawline = new THREE.Mesh(linegeometry, linematerial);
      clawline.position.y += 280;
      scene.add(clawline);

      //world
      world = new CANNON.World();
      world.gravity.set(0, -200, 0);
      world.broadphase = new CANNON.NaiveBroadphase();

      var groundShape = new CANNON.Plane();
      groundShape.updateBoundingSphereRadius();

      //牆壁(右)
      let rwallCM = new CANNON.Material();
      let rwallBody = new CANNON.Body({
        mass: 0,
        shape: groundShape,
        position: new THREE.Vector3(150, 0, 0),
        material: rwallCM,
      });
      rwallBody.quaternion.setFromAxisAngle(
        new CANNON.Vec3(0, 1, 0),
        -Math.PI / 2
      );
      world.add(rwallBody);

      //牆壁(左)
      let lwallCM = new CANNON.Material();
      let lwallBody = new CANNON.Body({
        mass: 0,
        shape: groundShape,
        position: new CANNON.Vec3(-150, 0, 0),
        material: lwallCM,
      });
      lwallBody.quaternion.setFromAxisAngle(
        new CANNON.Vec3(0, 1, 0),
        Math.PI / 2
      );
      world.add(lwallBody);

      //牆壁(前)
      let fwallCM = new CANNON.Material();
      let fwallBody = new CANNON.Body({
        mass: 0,
        shape: groundShape,
        position: new THREE.Vector3(0, 0, 150),
        material: fwallCM,
      });
      fwallBody.quaternion.setFromAxisAngle(new CANNON.Vec3(1, 0, 0), Math.PI);
      world.add(fwallBody);

      //牆壁(後)
      let bwallCM = new CANNON.Material();
      let bwallBody = new CANNON.Body({
        mass: 0,
        shape: groundShape,
        position: new THREE.Vector3(0, 0, -150),
        material: bwallCM,
      });
      world.add(bwallBody);

      //地面grid
      let groundCM = new CANNON.Material();
      let groundBody = new CANNON.Body({
        mass: 0,
        shape: groundShape,
        position: new THREE.Vector3(0, -100, 800),
        material: groundCM,
      });
      groundBody.quaternion.setFromAxisAngle(
        new CANNON.Vec3(1, 0, 0),
        -Math.PI / 2
      );
      world.add(groundBody);

      /*------------ 底部 --------*/
      //bott mesh
      let bottGeometry = new THREE.BoxGeometry(200, 100, 300);
      let bottMaterial = new THREE.MeshStandardMaterial({ color: 0x333333 });
      var bott = new THREE.Mesh(bottGeometry, bottMaterial);
      bott.position.x = 50;
      bott.position.y = -45;
      //scene.add(bott)

      //bott grid
      let bottCM = new CANNON.Material();
      var bottBody = new CANNON.Body({
        mass: 0,
        shape: new CANNON.Box(new CANNON.Vec3(100, 50, 150)),
        position: new THREE.Vector3(50, -45, 0),
        material: bottCM,
      });
      world.add(bottBody);

      //bott2 mesh
      let bottGeometry2 = new THREE.BoxGeometry(100, 100, 210);
      let bottMaterial2 = new THREE.MeshStandardMaterial({ color: 0x333333 });
      var bott2 = new THREE.Mesh(bottGeometry2, bottMaterial2);
      bott2.position.x = -100;
      bott2.position.y = -45;
      bott2.position.z = -40;
      //scene.add(bott2)

      // bott2 grid
      let bottCM2 = new CANNON.Material();
      var bottBody2 = new CANNON.Body({
        mass: 0,
        shape: new CANNON.Box(new CANNON.Vec3(50, 50, 105)),
        position: new THREE.Vector3(-100, -45, -40),
        material: bottCM2,
      });
      world.add(bottBody2);

      //黑塊
      let bottGeometry3 = new THREE.BoxGeometry(100, 10, 100);
      let bottMaterial3 = new THREE.MeshStandardMaterial({ color: 0x333333 });
      var bott3 = new THREE.Mesh(bottGeometry3, bottMaterial3);
      bott3.position.x = -100;
      bott3.position.y = -4;
      bott3.position.z = 98;
      scene.add(bott3);

      //右檔板
      var Bafflegeometry = new THREE.PlaneGeometry(100, 80);
      var Bafflematerial = new THREE.MeshPhongMaterial({
        color: 0xff11ff,
        transparent: true,
        opacity: 0.4,
        side: THREE.DoubleSide,
      });
      var Baffleplane = new THREE.Mesh(Bafflegeometry, Bafflematerial);
      Baffleplane.rotation.y = (90 * Math.PI) / 180;

      Baffleplane.position.x = -50;
      Baffleplane.position.y = 50;
      Baffleplane.position.z = 100;
      scene.add(Baffleplane);

      // 右檔板 grid
      let BafflebottCM = new CANNON.Material();
      var BafflebottBody = new CANNON.Body({
        mass: 0,
        shape: new CANNON.Box(new CANNON.Vec3(1, 40, 50)),
        position: new THREE.Vector3(-50, 50, 100),
        material: BafflebottCM,
      });
      world.add(BafflebottBody);

      //後檔板
      var Baffleplane2 = new THREE.Mesh(Bafflegeometry, Bafflematerial);
      Baffleplane2.position.x = -100;
      Baffleplane2.position.y = 50;
      Baffleplane2.position.z = 50;
      scene.add(Baffleplane2);

      //後檔板 grid
      let BafflebottCM2 = new CANNON.Material();
      var BafflebottBody2 = new CANNON.Body({
        mass: 0,
        shape: new CANNON.Box(new CANNON.Vec3(50, 40, 1)),
        position: new THREE.Vector3(-100, 50, 50),
        material: BafflebottCM2,
      });
      world.add(BafflebottBody2);

      var bodyTexture = new THREE.TextureLoader().load(this.play_info["url"]);
      var cm_array = [];
      var body_array = [];
      var mesh_array = [];
      var product_amount = JSON.parse(sessionStorage["play_info"])["amount"];

      for (let i = 0; i < product_amount; i++) {
        //物品body
        cm_array[i] = new CANNON.Material();
        body_array[i] = new CANNON.Body({
          mass: 5,
          shape: new CANNON.Box(new CANNON.Vec3(22, 22, 22)),
          position: new THREE.Vector3(50 + i * 2, 200 * i + 0, -50 + i * 2),
          material: cm_array[i],
        });
        world.add(body_array[i]);
        // 物品mesh
        mesh_array[i] = new THREE.Mesh(
          new THREE.BoxGeometry(44, 44, 44),
          new THREE.MeshStandardMaterial({ map: bodyTexture })
        );
        scene.add(mesh_array[i]);
      }

      /*夾子碰撞*/
      //box grid
      let boxCM = new CANNON.Material();
      var boxBody = new CANNON.Body({
        mass: 0,
        shape: new CANNON.Box(new CANNON.Vec3(19, 2.5, 2.5)),
        position: new THREE.Vector3(0, 0, 0),
        material: boxCM,
      });
      world.add(boxBody);

      //box2 grid
      let boxCM2 = new CANNON.Material();
      var boxBody2 = new CANNON.Body({
        mass: 0,
        shape: new CANNON.Box(new CANNON.Vec3(19, 2.5, 2.5)),
        position: new THREE.Vector3(0, 0, 0),
        material: boxCM2,
      });
      world.add(boxBody2);

      const timeStep = 1.0 / 60.0; // seconds

      /*renderer*/
      renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
      renderer.setClearColor(0xa0a0a0);
      renderer.setPixelRatio(window.devicePixelRatio);
      renderer.setSize(window.innerWidth, window.innerHeight);

      var controls = new TControls.TrackballControls(
        camera,
        renderer.domElement
      );
      controls.rotateSpeed = 1.0;
      controls.zoomSpeed = 1.2;
      controls.panSpeed = 0.2;
      controls.noZoom = false;
      controls.noPan = false;
      controls.staticMoving = false;
      controls.dynamicDampingFactor = 0.3;
      var radius = 100;
      controls.minDistance = 0.0;
      controls.maxDistance = radius * 1000;
      var SHADOW_MAP_WIDTH = 512;
      var SHADOW_MAP_HEIGHT = 512;
      var MARGIN = 0;
      var SCREEN_WIDTH = window.innerWidth;
      var SCREEN_HEIGHT = window.innerHeight - 2 * MARGIN;
      var NEAR = 5,
        FAR = 2000;
      var mouseX = 0,
        mouseY = 0;
      var windowHalfX = window.innerWidth / 2;
      var windowHalfY = window.innerHeight / 2;
      controls.screen.width = SCREEN_WIDTH;
      controls.screen.height = SCREEN_HEIGHT;

      animate();

      function animate() {
        if (document.getElementById("three") == null) return;
        document.getElementById("three").style.width = "1200px";
        document.getElementById("three").style.height = "750px";

        world.step(timeStep);

        controls.update();
        mesh_array.forEach((item, index) => {
          mesh_array[index].position.copy(body_array[index].position);
        });
        clawbody.rotation.y += 0.01;
        clawline.position.x = clawSystem.position.x;
        clawline.position.z = clawSystem.position.z;
        var axis = new CANNON.Vec3(1, 0, 0);
        var angle = clawMesh1.rotation.z + (50 * Math.PI) / 180;

        boxBody.position.x = clawSystem.position.x - 50;
        boxBody.position.y = clawSystem.position.y + 130;
        boxBody.position.z = clawSystem.position.z;
        boxBody.quaternion.setFromAxisAngle(axis, angle);

        boxBody2.position.x = clawSystem.position.x + 50;
        boxBody2.position.y = clawSystem.position.y + 130;
        boxBody2.position.z = clawSystem.position.z;
        boxBody2.quaternion.setFromAxisAngle(axis, angle);

        new_play_lock = that.play_lock;
        if (new_play_lock != old_play_lock && new_play_lock == false) {
          coin.position.set(94, -60, 280);
          coin.rotation.y = 0;
        }

        old_play_lock = new_play_lock;
        if (!that.play_lock && coin.position.y > -85) {
          if (coin.position.y == -60 && coin.rotation.y <= 8) {
            coin.rotation.y += 0.1;
          } else {
            coin.position.z -= 2;
            coin.position.y -= 1;
          }
        }

        /*爪子+搖桿*/
        if (up && !clawlock) {
          clawSystem.position.z -= 2;
          if (joystickSystem.rotation.x > -1) joystickSystem.rotation.x -= 0.1;
        }
        if (down && !clawlock) {
          clawSystem.position.z += 2;
          if (joystickSystem.rotation.x < 1) joystickSystem.rotation.x += 0.1;
        }
        if (left && !clawlock) {
          clawSystem.position.x -= 2;
          if (joystickSystem.rotation.z < 1) joystickSystem.rotation.z += 0.1;
        }
        if (right && !clawlock) {
          clawSystem.position.x += 2;
          if (joystickSystem.rotation.z > -1) joystickSystem.rotation.z -= 0.1;
        }
        if (!up && !down && !left && !right) {
          if (joystickSystem.rotation.x < 0) joystickSystem.rotation.x += 0.1;
          if (joystickSystem.rotation.x > 0) joystickSystem.rotation.x -= 0.1;
          if (joystickSystem.rotation.z < 0) joystickSystem.rotation.z += 0.1;
          if (joystickSystem.rotation.z > 0) joystickSystem.rotation.z -= 0.1;
        }

        /*爪子上下*/
        if (clawlock) {
          /* 下抓 */
          if (clawdown) {
            clawline.position.y -= 0.8;
            clawline.scale.y += 0.1;
            clawSystem.position.y -= 2;

            if (clawSystem.position.y <= -100 && !close && !clawup) {
              console.log(clawSystem.position.y, close, clawup);
              clawdown = false;
              close = true;
            }
          }

          /* 合爪 */

          if (close) {
            clawMesh1.rotation.z += 0.01;
            clawMesh2.rotation.z += 0.01;

            if (clawMesh2.rotation.z > 2) {
              body_array.forEach((i) => {
                if (
                  i.position.x < clawSystem.position.x + 15 &&
                  i.position.x > clawSystem.position.x - 15 &&
                  i.position.z < clawSystem.position.z + 15 &&
                  i.position.z > clawSystem.position.z - 15
                )
                  bingo = i;
              });

              close = false;
              clawup = true;
            }
          }

          /* 升爪 */
          if (clawup) {
            clawline.position.y += 0.8;
            clawline.scale.y -= 0.1;
            clawSystem.position.y += 2;
          }

          if (clawSystem.position.y == currentY) {
            clawup = false;
            backOrigin = true;
          }

          if (backOrigin) {
            if (clawSystem.position.x > -96) {
              clawSystem.position.x -= 1;
            } else if (clawSystem.position.z < 94) {
              clawSystem.position.z += 1;
            } else {
              clawMesh1.rotation.z = 1.5;
              clawMesh2.rotation.z = 1.5;
              bingo = undefined;
              setTimeout(function () {
                mesh_array.forEach((item, index) => {
                  if (item.position.y < -10) {
                    mesh_array.splice(index, 1);
                    scene.remove(item);
                  }
                });

                body_array.forEach((item, index) => {
                  if (item.position.y < -10) {
                    body_array.splice(index, 1);
                    world.remove(item);
                    that.axios
                      .post("/add_user_prize", {
                        user: that.user,
                        prize_info: JSON.parse(sessionStorage["play_info"])[
                          "id"
                        ],
                      })
                      .then((response) => {
                        that.$message({
                          message: "恭喜獲得獎品",
                          type: "success",
                        });
                      });
                  }
                });

                clawlock = false;
                that.play_lock = true;
                backOrigin = false;
              }, 1500);
            }
          }

          if (bingo != undefined) {
            bingo.position.x = clawSystem.position.x;
            bingo.position.z = clawSystem.position.z;
            bingo.position.y = clawSystem.position.y + 150;
          }
        }
        renderer.render(scene, camera);
        requestAnimationFrame(animate);
      }

      window.addEventListener("keydown", press);
      window.addEventListener("keyup", release);

      function press(e) {
        if (!that.play_lock) {
          var press_key = e["key"];
          if (press_key == "ArrowUp" /* ^ */) up = true;
          if (press_key == "ArrowDown" /* v */) down = true;
          if (press_key == "ArrowLeft" /* < */) left = true;
          if (press_key == "ArrowRight" /* > */) right = true;
          if (press_key == " ") {
            if (!clawlock) {
              currentY = clawSystem.position.y;
              clawlock = true;
              clawdown = true;
            }
          }
        }
      }

      function release(e) {
        if (!that.play_lock) {
          var press_key = e["key"];
          if (press_key == "ArrowUp" /* ^ */) up = false;
          if (press_key == "ArrowDown" /* v */) down = false;
          if (press_key == "ArrowLeft" /* < */) left = false;
          if (press_key == "ArrowRight" /* > */) right = false;
        }
      }
    },
  },
};
</script>