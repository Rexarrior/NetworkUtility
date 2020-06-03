<template>
  <div class="hello">
      <b-navbar toggleble="sd"  fixed="top" type="dark" variant="dark"  class = "navbar-main">
      <div class="navbar-header">
        <h3 class="navbar-caption">NetworkUtility</h3>
      </div>
      <div class="user-panel">
        
        <p>{{UserName}}</p>
      </div>
      <div class="login-panel" v-if="IsAuthorized">
        <b-button variant="outline-primary">
          Sign Out
        </b-button>
        
      </div>
      <div class="login-panel" v-else>
        <b-button variant="outline-primary">
          Sign In
        </b-button>
        <b-button variant="outline-primary">
          Sign Up
        </b-button>
        </div>
    </b-navbar>
  
  <div v-if="IsAuthorized">
    <b-jumbotron  class="ip-list-card" lead="Список ip">
         <!-- <p>{{DEBUG_OUT}}</p> -->
         <b-card-group v-for="ip in IpList" :key="ip.id">
         <b-card class="expr-card">
           <b-card-header >
              <b-link @click="pickIp(ip)">{{ip.ip}}</b-link>
           </b-card-header>
           <b-card-body>
             <p></p>
           </b-card-body>
           <b-card-footer>
             <b-link @click="deleteIp(ip)">Удалить</b-link>
           </b-card-footer>
           
         </b-card>
         </b-card-group>
    </b-jumbotron>

    <b-jumbotron class="work-area" >
      <b-tabs content-class="mt-3">
        <b-tab title="Выражение" active>
          <b-form @submit="onSubmit" @reset="onReset">
          <b-form-group
            id="input-group-1"
            label="Вычислить"
            label-for="input-1"
            description="Выражение, которое будет вычислено"
          >
            <b-form-input
              id="input-1"
              v-model="Expression.text"
              type="text"
              required
              placeholder="sqrt(x**2 + y**2)"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Название выражения" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="Expression.name"
              required
              placeholder="Distance"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-3" label="Список переменных" label-for="input-3">
            <b-form-input
              id="input-3"
              v-model="RawVariables"
              required
              placeholder="x:1,0.01, 10; y:-100, 10, 100; "
              description="Границы изменения переменных в выражении"

            ></b-form-input>
          </b-form-group>

          
          

            <b-button type="submit" variant="primary" class="control-button">Вычислить</b-button>
            <br>
            <b-button type="reset" variant="danger" class="control-button">Очистить</b-button>
          </b-form>
        </b-tab>
        <b-tab title="Результаты" v-if="IsResults" class="results-table">
           <b-container fluid class="table-container">
            <b-table
              :items="Results" 
              caption-top
            >
            </b-table>
           </b-container>
          </b-tab>
      </b-tabs>
    </b-jumbotron>
  </div>
  
  <div v-else>
    <h2>Требуется авторизация</h2>
  </div>
  
  </div>

</template>

<script>
export default {
  name: 'Workspace',
  props: {
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<<style scoped>
.navbar-caption{
  color: white;
}
.user-panel{
  padding-left: 75%;
  margin-right: 1%;
  margin-top: 10px;
  color:white;
}
.login-panel{
 
  max-width: 150px;
  min-width: 150px;
}
.ip-list{
  position: absolute;
  left: 5%;
  top: 10%;
  bottom: 5%;
  padding-bottom: 10%;
  width: 25%;
  font-size: 20;
  overflow: scroll
}
.work-area{
  position: absolute;
  left: 35%;
  top: 10%;
  bottom: 5%;
  padding-bottom: 10%;
  width: 45%;
  font-size: 20;
  overflow: scroll
}
</style>
