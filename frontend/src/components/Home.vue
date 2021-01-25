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
              <p>For more information visit website</p>
              <b-button-group>
                <b-button variant="primary" @click="getCust"
                  >Ping Custodian</b-button
                >
                <SidebarNewPolicy />
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
        <b-col v-for="policy in policyList" v-bind:key="policy.id">
          <b-card
            :title="policy.name"
            :img-src="policy.image"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem; min-width:350px;"
            class="mb-4"
          >
            <b-card-text>
              {{ policy.description }}
            </b-card-text>

            <b-button href="#" variant="outline-primary" size="sm"
              >Enact Policy</b-button
            >
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

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
