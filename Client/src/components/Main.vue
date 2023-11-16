<template>
    <div class="logo">
        <img src="../assets/logo.png" alt="Wipro logo" />
    </div>
    <div class="details">
        <h2>RFQ Splitter</h2>
    </div>
    <div class="files">
        <input type="file" ref="fileInput" accept=".xlsx, .xls, .csv" />
        <div class="buttons">
            <button :disabled="!fileInput" @click="uploadFile">Generate</button>
            <button :disabled="!fileDownload" @click="clearFiles">Clear</button>
        </div>
        <!--
        <div class="results" v-if="Object.keys(GPTresponse).length > 0">
            <div class="software">
                <h2>Software Requirement with Summary</h2>
                <p>{{ GPTresponse.software }}</p>
                <button :disabled="!fileDownload" @click="downloadFile" >Download</button>
            </div>
            <div class="hardware">
                <h2>Hardware Requirement with summary</h2>
                <p>{{ GPTresponse.hardware }}</p>
                <button :disabled="!fileDownload" @click="downloadFile" >Download</button>
            </div>
        </div>
        -->
        <div class="results" v-if="Object.keys(GPTresponse).length > 0">
            <div class="cards" v-for="(value, key) in GPTresponse" :key="key">
                <h2>{{ key }} Requirement with Summary</h2>
                <p style="white-space: pre-wrap;text-align: left;">{{ value }}</p>
                <button :disabled="!fileDownload" @click="downloadFile" >Download</button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const fileInput = ref(null);
const GPTresponse = ref({});
const fileDownload = ref(null);

const uploadFile = async () => {
    const file = fileInput.value.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('http://localhost:5000/upload', {
                method: 'POST',
                body: formData,
            });

            console.log('Server response:', response.status, response.statusText);
            fileDownload.value = await response.blob();
            getGPT();

            /*if(response.ok){
                const blob = await response.blob();

                const url = window.URL.createObjectURL(blob);
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'downloaded_file.xlsx');

                document.body.appendChild(link);
                link.click();

                document.body.removeChild(link);
                console.log('File downloaded');
            }*/

        } catch (error) {
            console.error('Error uploading file:', error);
        }
    } else {
        console.warn('No file selected');
    }
};

const clearFiles = () => {
    fileInput.value.value = '';
    fileDownload.value = null;
    GPTresponse.value = {};
};

const downloadFile = () => {
    const url = window.URL.createObjectURL(fileDownload.value);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'downloaded_file.xlsx');

    document.body.appendChild(link);
    link.click();

    document.body.removeChild(link);
    console.log('File downloaded');
}

const getGPT = async () => {
    try {
        const response = await fetch('http://localhost:5000/response', {
            method: 'GET',
        });

        console.log('Server response:', response.status, response.statusText);

        if(response.ok){
            GPTresponse.value = await response.json();
            console.log(GPTresponse.value);
        }

    } catch (error) {
        console.error('Error uploading file:', error);
    }
};

</script>

<style scoped>

    img{
        height:150px;
        width:240px;
    }

    .files{
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
    }

    .files input{
        width: 200px;
        outline: 2px solid rgb(138, 138, 174);
        margin: 5px;
    }

    .buttons{
        width: 200px;
        padding: 5px;
        display:flex;
        justify-content:space-between;
        align-items:center;
    }

    .results{
        width:100vw;
        display:flex;
        justify-content:space-around;
        align-items:center;
        flex-wrap: wrap;
    }

    .cards{
        max-width: 40%;
        max-height: 600px;
        overflow-y: scroll;
    }

    .cards::-webkit-scrollbar{
        display: none;
    }
    

</style>
