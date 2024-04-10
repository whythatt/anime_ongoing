import { reactive } from '@vue/reactivity';

const store = reactive({
    state: {
        user: null
    },
    setUser(userData) {
        store.state.user = userData;
    },
    getUser() {
        return store.state.user;
    }
});

export default store;
