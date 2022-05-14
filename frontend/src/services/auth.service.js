import { User } from "../models/user.model"

export class AuthService {
    setToken(token) {
        localStorage.setItem('dropshipify-token', token)
    }

    getToken() {
        return localStorage.getItem('dropshipify-token')
    }

    setUser(user) {
        localStorage.setItem('dropshipify-user', JSON.stringify(user))
    }

    getUser() {
        const user = localStorage.getItem('dropshipify-user')
        return user ? new User(JSON.parse(user)) : null
    }

    logout() {
        localStorage.removeItem('dropshipify-token')
        localStorage.removeItem('dropshipify-user')
    }
}