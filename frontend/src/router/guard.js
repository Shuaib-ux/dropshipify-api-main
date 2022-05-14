import { notificationService } from "../services/notification.service";
import store from "../store";

export const authGuard = (to, next) => {
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        store.dispatch('authModule/getUser')
            .then(() => {
                next()
            })
            .catch(() => {
                notificationService.error('Your token has expired. Please log in')
                store.dispatch('authModule/logout')
                next({ name: 'Login' })
            })
    } else {
        next();
    }
};

export const retailerGuard = (to, next) => {
    if (to.matched.some((record) => record.meta.isRetailer)) {
        if (store.state.authModule.isRetailer) {
            next()
        } else {
            notificationService.error('This page is only accessible to retailers')
            notificationService.error('Create a store to proceed.')
            next({ name: 'Register Retailer' })
        }
    } else {
        next();
    }
};

export const metaWrapper = (to, from) => {
    const nearestWithTitle = to.matched
        .slice()
        .reverse()
        .find((r) => r.meta && r.name);

    const nearestWithMeta = to.matched
        .slice()
        .reverse()
        .find((r) => r.meta && r.meta.metaTags);

    const previousNearestWithMeta = from.matched
        .slice()
        .reverse()
        .find((r) => r.meta && r.meta.metaTags);

    if (nearestWithTitle) {
        document.title = nearestWithTitle.meta.name || nearestWithTitle.name;
    } else if (previousNearestWithMeta) {
        document.title = previousNearestWithMeta.meta.name || previousNearestWithMeta.name;
    }

    Array.from(
        document.querySelectorAll("[data-vue-router-controlled]")
    ).map((el) => el.parentNode?.removeChild(el));

    if (nearestWithMeta) {
        appendTags(nearestWithMeta.meta.metaTags);
    }

};

export function appendTags(tags) {
    tags
        .map((tagDef) => {
            const tag = document.createElement("meta");

            Object.keys(tagDef).forEach((key) => {
                tag.setAttribute(key, tagDef[key]);
            });

            tag.setAttribute("data-vue-router-controlled", "");

            return tag;
        })
        .forEach((tag) => document.head.appendChild(tag));
}