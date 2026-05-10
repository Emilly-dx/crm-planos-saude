// Função para editar a linha
function editarLinha(botao) {
    const linha = botao.closest('tr');           // pega a <tr> atual
    const celulas = linha.querySelectorAll('td'); // todas as células da linha

    // Colunas que queremos editar (ajuste os índices conforme sua tabela)
    // 0=Nome, 1=Telefone, 2=Grávida, 3=Nascimento, 4=Altura, 5=Peso, 6=CPF, 7=RG, 8=Status, 9=Retorno
    const indicesEditaveis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

    // Guarda os valores originais e transforma em inputs
    celulas.forEach((celula, index) => {
        if (indicesEditaveis.includes(index)) {
            const valorOriginal = celula.textContent.trim();
            
            if (index === 2) { // Grávida (Sim/Não)
                celula.innerHTML = `
                    <select class="edit-input w-full border border-sky-400 rounded px-2 py-1">
                        <option value="Sim" ${valorOriginal === "Sim" ? "selected" : ""}>Sim</option>
                        <option value="Não" ${valorOriginal === "Não" ? "selected" : ""}>Não</option>
                    </select>`;
            } else if (index === 8) { // Status (select)
                celula.innerHTML = `
                    <select class="edit-input w-full border border-sky-400 rounded px-2 py-1">
                        <option ${valorOriginal === "Interessado" ? "selected" : ""}>Interessado</option>
                        <option ${valorOriginal === "Em negociação" ? "selected" : ""}>Em negociação</option>
                        <option ${valorOriginal === "Fechado" ? "selected" : ""}>Fechado</option>
                        <option ${valorOriginal === "Perdido" ? "selected" : ""}>Perdido</option>
                    </select>`;
            } else {
                celula.innerHTML = `
                    <input type="text" value="${valorOriginal}" 
                           class="edit-input w-full border border-sky-400 rounded px-3 py-1 text-sm">`;
            }
        }
    });

    // Troca os botões: Pen → Salvar + Cancelar
    const acoes = linha.querySelector('td:last-child .flex');
    acoes.innerHTML = `
        <button onclick="salvarEdicao(this)" class="text-emerald-600 hover:text-emerald-700">
            <i class="fa-solid fa-check text-lg"></i>
        </button>
        <button onclick="cancelarEdicao(this)" class="text-gray-500 hover:text-gray-700">
            <i class="fa-solid fa-xmark text-lg"></i>
        </button>
    `;
}

// Função para salvar a edição
function salvarEdicao(botao) {
    const linha = botao.closest('tr');
    const inputs = linha.querySelectorAll('.edit-input');

    // Atualiza as células com os novos valores
    Array.from(inputs).forEach((input, i) => {
        const celula = input.closest('td');
        celula.textContent = input.value || input.options[input.selectedIndex].text;
    });

    // Restaura os botões originais de editar/excluir
    const acoes = linha.querySelector('td:last-child .flex');
    acoes.innerHTML = `
        <button onclick="editarLinha(this)" class="text-sky-600 hover:text-sky-800 transition-colors">
            <i class="fa-solid fa-pen text-lg"></i>
        </button>
        <button onclick="if(confirm('Excluir cliente?')) this.closest('tr').remove()" 
                class="text-red-500 hover:text-red-700 transition-colors">
            <i class="fa-solid fa-trash text-lg"></i>
        </button>
    `;

    // Aqui você pode adicionar um fetch() para enviar os dados atualizados para o backend
    // console.log('Dados atualizados da linha:', getDadosLinha(linha));
}

// Função auxiliar para cancelar (volta ao estado original)
function cancelarEdicao(botao) {
    const linha = botao.closest('tr');
    window.location.reload(); // solução simples: recarrega a página (não ideal em produção)
    // Para uma solução melhor sem recarregar, você precisaria guardar os valores originais antes de editar.
}



// ====================== GERENCIAMENTO DE CLIENTES NO FRONTEND ======================

let clientes = [];

// Carrega clientes do localStorage ou dos dados iniciais do backend
function carregarClientes() {
    const salvos = localStorage.getItem('meusClientes');
    
    if (salvos) {
        clientes = JSON.parse(salvos);
    } else {
        // Pega os clientes que vieram do backend na primeira carga
        clientes = Array.from(document.querySelectorAll('#section-clientes tbody tr')).map(tr => {
            const celulas = tr.querySelectorAll('td');
            return {
                nome: celulas[0].textContent.trim(),
                telefone: celulas[1].textContent.trim(),
                gravida: celulas[2].textContent.trim(),
                data_nascimento: celulas[3].textContent.trim(),
                altura: celulas[4].textContent.trim(),
                peso: celulas[5].textContent.trim(),
                cpf: celulas[6].textContent.trim(),
                rg: celulas[7].textContent.trim(),
                status: celulas[8].textContent.trim(),
                retorno: celulas[9].textContent.trim()
            };
        });
        salvarClientes();
    }
    
    renderizarTabela();
}

// Salva no localStorage
function salvarClientes() {
    localStorage.setItem('meusClientes', JSON.stringify(clientes));
}

// Renderiza a tabela novamente
function renderizarTabela() {
    const tbody = document.querySelector('#section-clientes tbody');
    tbody.innerHTML = '';

    clientes.forEach((cliente, index) => {
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-gray-50 transition-colors';
        tr.innerHTML = `
            <td>${cliente.nome}</td>
            <td>${cliente.telefone}</td>
            <td>${cliente.gravida}</td>
            <td>${cliente.data_nascimento}</td>
            <td>${cliente.altura}</td>
            <td>${cliente.peso}</td>
            <td>${cliente.cpf}</td>
            <td>${cliente.rg}</td>
            <td>${cliente.status}</td>
            <td>${cliente.retorno}</td>
            <td class="px-5 py-4 text-right">
                <div class="flex items-center justify-end gap-4">
                    <button onclick="editarLinha(this)" class="text-sky-600 hover:text-sky-800 transition-colors">
                        <i class="fa-solid fa-pen text-lg"></i>
                    </button>
                    <button onclick="excluirCliente(this)" class="text-red-500 hover:text-red-700 transition-colors">
                        <i class="fa-solid fa-trash text-lg"></i>
                    </button>
                </div>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

// Função de excluir (agora persiste!)
function excluirCliente(botao) {
    if (!confirm('Tem certeza que deseja excluir este cliente?')) return;

    const linha = botao.closest('tr');
    const index = Array.from(linha.parentNode.children).indexOf(linha);
    
    clientes.splice(index, 1);     // Remove do array
    salvarClientes();              // Salva no localStorage
    renderizarTabela();            // Atualiza a tabela
}

// ====================== CHAMADA INICIAL ======================
document.addEventListener('DOMContentLoaded', () => {
    carregarClientes();
});
