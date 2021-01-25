<template>
  <div>
    <b-button v-b-toggle.sidebar variant="outline-primary"
      >Create a Policy</b-button
    >
    <b-sidebar id="sidebar" title="Create a new Policy" width="100%" v-model="sideBarVis">
      <div class="px-5 py-5">
        <b-form-group
          label="Policy Name"
          description="Enter Name of Policy"
          :label-cols="3"
        >
          <b-form-input
            placeholder="e.g.- Trim unused instances"
            v-model.trim="policyName"
            :state="policyName.length < 50"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          label="Policy Description"
          description="Enter Description of Policy"
          :label-cols="3"
        >
          <b-form-textarea
            class="mt-3"
            id="textarea"
            v-model="policyDesc"
            placeholder="e.g.- Shutdown all instances that are not running"
            rows="3"
            max-rows="6"
            :state="policyDesc.length < 350"
            no-resize
          ></b-form-textarea>
        </b-form-group>

        <b-form-group
          label="Cloud Provider"
          description="Select Cloud Provider"
          :label-cols="3"
        >
          <cloud-select
            v-model="selected"
            @selected="onCloudSelect"
          ></cloud-select>
        </b-form-group>

        <b-form-group
          label="Policy Script"
          description="Enter Policy Script"
          :label-cols="3"
        >
          <MonacoEditor
            height="300"
            theme="vs-dark"
            language="yaml"
            :options="options"
            @change="handleValidate"
          ></MonacoEditor>
        </b-form-group>

        <b-form-group
          label="Script Validation Status"
          description=""
          :label-cols="3"
        >
          <pre><small
            v-bind:style="[valid.valid ? { color: 'green' } : { color: 'red' }]"
            >{{ valid.output }}</small
          ></pre>
        </b-form-group>

        <b-row>
          <b-col cols="auto" class="ml-auto">

            <b-button
              variant="outline-secondary"
              visible="sideBarVis"
              @click="cancelCreate"
            >Cancel</b-button>
            <b-button
              v-bind:variant="[valid.valid ? 'success' : 'danger']"
              :disabled="!valid.valid"
              @click="save"
              >Save policy</b-button
            >
          </b-col>
        </b-row>
      </div>
    </b-sidebar>
  </div>
</template>

<script>
import axios from "axios";
import CloudSelect from "./CloudSelect";
import MonacoEditor from "monaco-editor-vue";

export default {
  components: {
    CloudSelect,
    MonacoEditor
  },
  data() {
    return {
      selected: undefined,
      sideBarVis: false,
      valid: "",
      policyName: "",
      policyDesc: "",
      policyCloud: "",
      policyScript: "",
      options: {
        automaticLayout: true
      } // monaco editor options
    };
  },
  methods: {
    cancelCreate(){
      this.sideBarVis = false;
    },
    handleValidate(value) {
      this.policyScript = value;
      this.valid = this.validateScript();
    },
    validateScript() {
      const path = "http://localhost:5000/api/validate";
      axios
        .post(path, { data: this.policyScript })
        .then(response => {
          this.valid = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    save() {
      this.policy = this.savePolicy();
    },
    onCloudSelect(value) {
      this.policyCloud = value;
    },
    savePolicy() {
      const path = "http://localhost:5000/api/policy";
      const data = {
        name: this.policyName,
        description: this.policyDesc,
        cloud: this.policyCloud,
        yaml: this.policyScript
      };
      axios
        .post(path, data)
        .then(response => {
          console.log(response.data);
          this.$bvToast.toast(`Successfully saved ${this.policyName}`, {
            title: "Success",
            autoHideDelay: 2000,
            variant: "success"
          });
          this.sideBarVis = false;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>
