import axios from "axios";
import store from "../store";
import { AuthService } from "./auth.service";
import { notificationService } from './notification.service';

const config = {
    baseURL: 'https://flask-dropshipfy-api.herokuapp.com/',
    //baseURL: 'http://127.0.0.1:5000/',
    headers: {
        'Content-Type': 'application/json'
    }
}

let activeRequests = 0;
const authService = new AuthService();
const httpService = axios.create(config)

httpService.interceptors.request.use(
    (config) => {
        if (activeRequests === 0) {
            store.dispatch('loadingModule/startLoading')
        }

        const token = authService.getToken()

        if (token) {
            config.headers = { 'Authorization': `Bearer ${token}` }
        }

        activeRequests++

        return config;
    }
)

httpService.interceptors.response.use(
    (response) => {
        activeRequests--
        if (activeRequests === 0) {
            store.dispatch('loadingModule/stopLoading')
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

export { httpService }