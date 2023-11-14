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
            <button @click="uploadFile">Update</button>
            <button @click="clearFiles">Clear</button>
        </div>
        <p>{{ GPTresponse }}</p>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const fileInput = ref(null);
const GPTresponse = ref('');

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
            getGPT();

            if(response.ok){
                const blob = await response.blob();

                const url = window.URL.createObjectURL(blob);
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'downloaded_file.xlsx');

                document.body.appendChild(link);
                link.click();

                document.body.removeChild(link);
                console.log('File downloaded');
            }

        } catch (error) {
            console.error('Error uploading file:', error);
        }
    } else {
        console.warn('No file selected');
    }
};

const clearFiles = () => {
    fileInput.value.value = '';
};

const getGPT = async () => {
    try {
        const response = await fetch('http://localhost:5000/response', {
            method: 'GET',
        });

        console.log('Server response:', response.status, response.statusText);

        if(response.ok){
            GPTresponse.value = await response.text();
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
    

</style>
