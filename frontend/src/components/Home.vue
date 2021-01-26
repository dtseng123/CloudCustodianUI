<template>
 
  <div>
    <b-container fluid>
      <b-row>
        <b-col>
          <div>
            <b-jumbotron
              header="Cloud Custodian UI"
              lead="Cloud Policy Management"
            >
              <p>This tool is meant to be a locally installed light UI client for managing Cloud Custodian Policies.</p>
              <p>Prerequisites: Make sure you have Cloud Custodian cli tool installed and permission authorized for your cloud.</p>
              <b-button-group>
                <b-button variant="primary" @click="getCust"
                  >Ping Custodian</b-button
                >
                <SidebarNewPolicy @savedSuccess="savedSuccess"/>
              </b-button-group>
            </b-jumbotron>
          </div>
        </b-col>
      </b-row>
    </b-container>
    <b-container>
      <b-row>
        <b-col>
          <pre
            style="background:#232323; padding:15px; color:white; border-radius:8px;"
            >{{ custodian }}</pre
          >
        </b-col>

      </b-row>
     
    </b-container>
    <hr />
    <b-container class="mt-5">
      <b-row>
        <b-col lg="3" md="4" sm="12" v-for="policy in policyList" v-bind:key="policy.id">
          <b-card
            :title="policy.name"
            :img-src="policy.image"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;  "
            class="mb-4"
          >
          <b-badge class="cloud-badge" size="sm" variant="success"><b-icon-cloud-fill></b-icon-cloud-fill> {{policy.cloud}}</b-badge>
            <b-card-text>
              {{ policy.description }}
            </b-card-text>
            <b-button-group>
              <b-button @click="deployPolicy(policy)" variant="outline-primary" size="sm"
                >Enact Policy</b-button
              >
              <!-- <b-button href="#" variant="outline-secondary" size="sm"
                >View </b-button
              >
              <b-button href="#" variant="outline-secondary" size="sm"
                >Edit </b-button
              > -->
              <b-button @click="deletePolicy(policy)" variant="outline-danger" size="sm"
                >Delete </b-button
              >
            </b-button-group>  
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<style>
  .card-title{
    left:0;
    position:absolute;
    color:#333333;
    text-transform: capitalize;
    top:20px;
    background: rgba(255, 255, 255,0.8);
    padding: 3px 20px;
    font-size:18px;
    font-weight:300;
  }

</style>

<script>
import axios from "axios";
import SidebarNewPolicy from "./SidebarNewPolicy";

export default {
  components: {
    SidebarNewPolicy
  },
  data() {
    return {
    
      policy: {},
      custodian: "",
      policyList: [
        {
          id: 0,
          name: "policy 123",
          description: "policy description here!!"
        }
      ],

    };
  },

  methods: {
    getCust() {
      this.custodian = this.getCustodian();
    },
    getCustodian() {
      const path = "http://localhost:5000/api/custodian";
      axios
        .get(path)
        .then(response => {
          this.custodian = response.data.custodian;

          this.$bvToast.toast(`Successfully pinged custodian`, {
            title: "Success",
            autoHideDelay: 2000,
            variant: "success"
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    deployPolicy(policy){
      const path =`http://localhost:5000/api/policy/deploy/${policy.id}`;
       axios
        .post(path)
        .then(response => {
        
        if(response.data.valid) {
            this.$bvToast.toast(`Successfully deployed ${policy.name} policy` , {
              title: "Success",
              variant: "success"
            });
        }
        else{
          this.$bvToast.toast(`${response.data.output}`, {
            title: "Failed",
            variant: "warning"
          });
        }
        })
        .catch(error => {
          console.log(error);
          this.$bvToast.toast(`There was a problem with deploying ${policy.name} policy: ${error}`, {
            title: "Failed",
            autoHideDelay: 2000,
            variant: "warning"
          });
        });
    },

    deletePolicy(policy){
      path = `http://localhost:5000/api/policy/${policy.id}`;
      axios
        .delete(path)
        .then(response => {
          this.$bvToast.toast(`Successfully deleted ${policy.name} policy` , {
            title: "Success",
            autoHideDelay: 2000,
            variant: "success"
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
  savedSuccess(){
    console.log("!!!","refreshed?!")
    this.created()
  },

  async created() {
    try {
      const response = await axios.get("http://localhost:5000/api/policy");

      // get different images, otherwise each image is the same
      this.policyList = response.data.map((p, idx) => {
        p.image = `https://picsum.photos/600/300?random=${idx}`;
        return p;
      });
    } catch (err) {
      this.error = err;
    }
  }
};
</script>
