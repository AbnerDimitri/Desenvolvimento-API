document.getElementById('editForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    // Coleta os dados do formulário
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const passwordConfirmation = document.getElementById('password_confirmation').value;

    // Validação simples para garantir que as senhas coincidam
    if (password !== passwordConfirmation) {
        document.getElementById('mensagem').innerHTML = '<div class="alert alert-danger">As senhas não coincidem.</div>';
        return;
    }

    // Aqui você deve adicionar a lógica para enviar os dados para o servidor
    fetch('/api/atualizar-usuario', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email, password }),
    })
    fetch('http://localhost:8000/api/atualizar', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data), })

    .then(response => {
        if (!response.ok) {
            throw new Error('Erro na atualização do usuário');
        }
        return response.json();
    })
    .then(data => {
        // Exibir mensagem de sucesso
        document.getElementById('mensagem').innerHTML = '<div class="alert alert-success">Usuário atualizado com sucesso!</div>';
    })
    .catch(error => {
        console.error('Erro:', error);
        document.getElementById('mensagem').innerHTML = '<div class="alert alert-danger">Erro ao atualizar usuário: ' + error.message + '</div>';
    });
});
