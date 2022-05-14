import axios from "axios";
import store from "../store";
import { notificationService } from './notification.service';

const config = {
    baseURL: 'https://amazon-products1.p.rapidapi.com/',
    headers: {
        'Content-Type': 'application/json',
        'X-RapidAPI-Host': 'amazon-products1.p.rapidapi.com',
        'X-RapidAPI-Key': '65e4bd2e37msh703ca32d6371974p1dbf4fjsn48f2593206a5'
    }
}

let activeRequests = 0;
const amazonService = axios.create(config)

amazonService.interceptors.request.use(
    (config) => {
        if (activeRequests === 0) {
            store.dispatch('loadingModule/startLoading')
        }

        activeRequests++

        return config;
    }
)

amazonService.interceptors.response.use(
    (response) => {
        activeRequests--
        if (activeRequests === 0) {
            store.dispatch('loadingModule/stopLoading')
        }

        if (response.data.error == true) {
            notificationService.error(response.data.message)
            return Promise.reject(response)
        }

        return response
    },
    (error) => {
        activeRequests--

        if (activeRequests === 0) {
            store.dispatch('loadingModule/stopLoading')
        }

        // const type = error.response?.data?.error;
        const message = error.response?.data?.message;
        const code = parseInt(error.response && error.response.status);

        console.log(message, code);

        if (code === 401) {
            // Throw Unauthorized Error Message
        } else if (code === 404) {
            notificationService.error(message)
        } else if (code === 500 || !code) {
            notificationService.error('Something went wrong')
        }

        return Promise.reject(error);
    }
)

export { amazonService }