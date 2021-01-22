

<template>
 
  <div>
 
    <b-container fluid>
    <b-row>
      <b-col> 
        <div>
          <b-jumbotron header="Cloud Custodian UI" lead="Cloud Policy Management">
            <p>For more information visit website</p>
            <b-button variant="primary" @click="getCust">Ping Custodian</b-button>
           </b-jumbotron>
        </div>
      </b-col>
    </b-row>
    </b-container>
    <b-container>
      <b-row >
        <b-col>
          <pre style="background:#232323; padding:15px; color:white; border-radius:8px;">{{ custodian }}</pre>
        </b-col>
      </b-row>

      <b-row >
        <b-col>
          <div>
            <b-form-group  label="Policy Name" description="Enter Name of Policy" :label-cols="4">
              <b-form-input placeholder="Trim unused instances" v-model.trim="policyName"></b-form-input>
            </b-form-group>

            <b-form-group  label="Policy Description" description="Enter Description of Policy" :label-cols="4">
              <b-form-textarea
                class="mt-3"
                id="textarea"
                v-model="policyDesc"
                placeholder="Shutdown all instances that are not running"
                rows="3"
                max-rows="6"
              ></b-form-textarea>
            </b-form-group>

            <b-form-group label="Cloud Provider" description="Select Cloud Provider" :label-cols="4">
              <cloud-select v-model="selected"  @selected="onCloudSelect">> </cloud-select>
            </b-form-group>

            <b-form-group  label="Policy Script" description="Enter policy script" :label-cols="4">
              <b-form-textarea
                class="mt-3"
                id="textarea"
                v-model="policyScript"
                placeholder="YAML"
                rows="10"
             
              ></b-form-textarea>
            </b-form-group>
             <b-button variant="primary" @click="save">Save policy</b-button>
          </div>
           

         </b-col>
      </b-row>
    </b-container>
    <hr/>
    <b-container class="mt-5">
      <b-row>
        <b-col v-for="policy in policyList" v-bind:key="policy.id">
            <b-card
              :title="policy.name"
              img-src="https://picsum.photos/600/300"
              img-alt="Image"
              img-top
              tag="article"
              style="max-width: 20rem; min-width:350px;"
              class="mb-4"
            >
              <b-card-text>
                 {{policy.description}}
              </b-card-text>

              <b-button href="#" variant="outline-primary" size="sm">Enact Policy</b-button>
            </b-card>
        </b-col>
        
      </b-row>
    </b-container>
   </div>
</template>

<script>

import axios from 'axios'
import CloudSelect from './CloudSelect'

export default {
components:{
  CloudSelect
},
data () {
    return {
      selected:undefined,
      policy:{},
      custodian:'',
      policyName:'',
      policyDesc:'',
      policyCloud:'',
      policyScript:'',
      policyList:[{
        id:0,
        name:"policy 123",
        description:"policy description here!!"
      }] 
    }
  },



  methods: {
    save(){
      this.policy= this.savePolicy() 
    },

    getCust (){
      this.custodian = this.getCustodian()
    },
    onCloudSelect(value){
      this.policyCloud =value
    },
    getCustodian (){
      const path = 'http://localhost:5000/api/custodian'
      axios.get(path)
      .then(response => {
        this.custodian = response.data.custodian
         
        this.$bvToast.toast(`Successfully pinged custodian`, {
          title: 'Success',
          autoHideDelay: 2000,
          variant: "success"
        })
        
      })
        .catch(error => {
        console.log(error)
      })
    }, 
 
    savePolicy(){
      const path = 'http://localhost:5000/api/policy'
      const data = { 
        name:this.policyName,
        description: this.policyDesc,
        cloud:this.policyCloud,
        yaml: this.policyScript
      }
      axios.post(path, data)
        .then(response => {
          console.log(response.data)

        })
        .catch(error => {
          console.log(error)
        })
    },
 
  },
  async created() {
    try {
      const response = await axios.get('http://localhost:5000/api/policy', )
      console.log("GET POLICIES",response.data)
      this.policyList = response.data
    } catch (err) {
      this.error = err
    }
 
  },
}
</script>