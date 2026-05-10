if (localStorage.getItem('logado') === 'true') {
        document.getElementById('logged-in').checked = true;
    }
    


    // Verifica se já está logado ao carregar a página
    if (localStorage.getItem('logado') === 'true') {
        document.getElementById('logged-in').checked = true;
    }

    // Função de Logout
    function logout() {
        localStorage.removeItem('logado');           // Remove o login salvo
        document.getElementById('logged-in').checked = false;  // Desmarca o checkbox
        window.location.reload();                    // Recarrega a página
    }
