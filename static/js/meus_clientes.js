// Função para alternar modo edição
function toggleEditar(id) {
    const linha = document.getElementById('linha-' + id);
    const viewCells = linha.querySelectorAll('.view-mode');
    const editCells = linha.querySelectorAll('.edit-mode');
    const btnSalvar = linha.querySelector('.btn-salvar-' + id);
    const btnCancelar = linha.querySelector('.btn-cancelar');
    const btnEditar = linha.querySelector('.btn-editar');

    viewCells.forEach(td => td.classList.add('hidden'));
    editCells.forEach(td => td.classList.remove('hidden'));
    btnSalvar.classList.remove('hidden');
    btnCancelar.classList.remove('hidden');
    btnEditar.classList.add('hidden');
}

function cancelarEdicao(id) {
    const linha = document.getElementById('linha-' + id);
    const viewCells = linha.querySelectorAll('.view-mode');
    const editCells = linha.querySelectorAll('.edit-mode');
    const btnSalvar = linha.querySelector('.btn-salvar-' + id);
    const btnCancelar = linha.querySelector('.btn-cancelar');
    const btnEditar = linha.querySelector('.btn-editar');

    viewCells.forEach(td => td.classList.remove('hidden'));
    editCells.forEach(td => td.classList.add('hidden'));
    btnSalvar.classList.add('hidden');
    btnCancelar.classList.add('hidden');
    btnEditar.classList.remove('hidden');
}

document.addEventListener('click', function(e) {
    const btnEditar = e.target.closest('.btn-editar');
    if (btnEditar) toggleEditar(btnEditar.dataset.id);

    const btnCancelar = e.target.closest('.btn-cancelar');
    if (btnCancelar) cancelarEdicao(btnCancelar.dataset.id);
});