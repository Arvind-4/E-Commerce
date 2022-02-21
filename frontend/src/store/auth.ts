export var is_authenticated = document.getElementById('is_authenticated')?.textContent

export function logoutUser() {
    if (confirm('Do you want to Logout? ')) {
        window.location.href = '/accounts/sign-out/'
    }
}