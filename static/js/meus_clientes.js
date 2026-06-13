/// ÁREA DE EDIÇÃO DE CLIENTES

document.querySelectorAll('.btn-editar').forEach(btn => {

    btn.addEventListener('click', () => {

        document.getElementById('editNome').value =
            btn.dataset.nome || '';

        document.getElementById('editTelefone').value =
            btn.dataset.telefone || '';

        document.getElementById('editGravida').value =
            btn.dataset.gravida === '1' ? 'Sim' : 'Não';

        document.getElementById('editNascimento').value =
            btn.dataset.data_nascimento || '';

        document.getElementById('editAltura').value =
            btn.dataset.altura_cm || '';

        document.getElementById('editPeso').value =
            btn.dataset.peso_kg || '';

        document.getElementById('editCpf').value =
            btn.dataset.cpf || '';

        document.getElementById('editRg').value =
            btn.dataset.rg || '';

        document.getElementById('editStatus').value =
            btn.dataset.status || '';

        document.getElementById('formEditar').action =
            `/clientes/${btn.dataset.id}`;

        document
            .getElementById('modalEditar')
            .classList.remove('hidden');
    });

});

function fecharModal() {

    document
        .getElementById('modalEditar')
        .classList.add('hidden');

}

/// ÁREA DE BUSCA DOS CLIENTES

(function() {
    function coletarClientes() {
        const linhas = document.querySelectorAll('#section-clientes tbody tr[id^="linha-"]');
        const clientes = [];
        linhas.forEach(linha => {
            const colunas = linha.querySelectorAll('td.view-mode');
            if (colunas.length >= 2) {
                clientes.push({
                    id: linha.id.replace('linha-', ''),
                    nome: colunas[0]?.textContent.trim() || '',
                    telefone: colunas[1]?.textContent.trim() || '',
                    gravida: colunas[2]?.textContent.trim() || '',
                    nascimento: colunas[3]?.textContent.trim() || '',
                    cpf: colunas[6]?.textContent.trim() || '',
                    status: colunas[8]?.textContent.trim() || '',
                    elemento: linha
                });
            }
        });
        return clientes;
    }

    function gerarItemResultado(cliente, termoBusca) {
        const termo = termoBusca.toLowerCase();
        function highlight(texto) {
            if (!texto) return '';
            const idx = texto.toLowerCase().indexOf(termo);
            if (idx === -1) return texto;
            return texto.slice(0, idx) +
                   '<mark style="background:#d1fae5;color:#065f46;border-radius:3px;padding:0 2px">' +
                   texto.slice(idx, idx + termo.length) +
                   '</mark>' +
                   texto.slice(idx + termo.length);
        }

        const statusCor = {
            'Interessado': 'bg-yellow-100 text-yellow-700',
            'Em negociação': 'bg-blue-100 text-blue-700',
            'Fechado': 'bg-green-100 text-green-700',
            'Perdido': 'bg-red-100 text-red-700'
        };
        const cor = statusCor[cliente.status] || 'bg-gray-100 text-gray-600';

        return `
        <div class="resultado-item px-4 py-3 hover:bg-gray-50 cursor-pointer border-b border-gray-100 last:border-0 transition-colors"
             data-id="${cliente.id}">
            <div class="flex items-center justify-between gap-3">
                <div class="min-w-0">
                    <p class="font-semibold text-sm text-gray-800 truncate">${highlight(cliente.nome)}</p>
                    <p class="text-xs text-gray-500 mt-0.5">${highlight(cliente.telefone)}
                        ${cliente.cpf ? `<span class="mx-1">·</span>${highlight(cliente.cpf)}` : ''}
                    </p>
                </div>
                ${cliente.status ? `<span class="text-xs px-2 py-0.5 rounded-full flex-shrink-0 ${cor}">${cliente.status}</span>` : ''}
            </div>
        </div>`;
    }

    function executarBusca(termo, inputEl, containerEl) {
        if (!termo || termo.length < 1) {
            containerEl.classList.add('hidden');
            return;
        }

        const clientes = coletarClientes();
        const termoLower = termo.toLowerCase();

        const encontrados = clientes.filter(c =>
            c.nome.toLowerCase().includes(termoLower) ||
            c.telefone.includes(termoLower) ||
            c.cpf.toLowerCase().includes(termoLower) ||
            c.status.toLowerCase().includes(termoLower) ||
            c.nascimento.includes(termoLower)
        );

        if (encontrados.length === 0) {
            containerEl.innerHTML = `<p class="px-4 py-3 text-sm text-gray-400">Nenhum cliente encontrado.</p>`;
        } else {
            containerEl.innerHTML = encontrados.map(c => gerarItemResultado(c, termo)).join('');
            containerEl.querySelectorAll('.resultado-item').forEach(item => {
                item.addEventListener('click', () => {
                    const id = item.dataset.id;
                    const linhaAlvo = document.getElementById('linha-' + id);
                    if (linhaAlvo) {
                        document.getElementById('section-clientes').scrollIntoView({ behavior: 'smooth' });
                        setTimeout(() => {
                            linhaAlvo.scrollIntoView({ behavior: 'smooth', block: 'center' });
                            linhaAlvo.style.transition = 'background 0.3s';
                            linhaAlvo.style.background = '#d1fae5';
                            setTimeout(() => { linhaAlvo.style.background = ''; }, 2000);
                        }, 300);
                    }
                    containerEl.classList.add('hidden');
                    inputEl.value = '';
                    document.getElementById('buscaMobileContainer').classList.add('hidden');
                });
            });
        }
        containerEl.classList.remove('hidden');
    }

    const campoBusca = document.getElementById('campoBusca');
    const resultadosBusca = document.getElementById('resultadosBusca');

    campoBusca.addEventListener('input', () => {
        executarBusca(campoBusca.value.trim(), campoBusca, resultadosBusca);
    });

    document.addEventListener('click', (e) => {
        if (!campoBusca.contains(e.target) && !resultadosBusca.contains(e.target)) {
            resultadosBusca.classList.add('hidden');
        }
    });

    const btnMobile = document.getElementById('btnBuscaMobile');
    const buscaMobileContainer = document.getElementById('buscaMobileContainer');
    const campoBuscaMobile = document.getElementById('campoBuscaMobile');
    const resultadosMobile = document.getElementById('resultadosBuscaMobile');

    btnMobile.addEventListener('click', () => {
        buscaMobileContainer.classList.toggle('hidden');
        if (!buscaMobileContainer.classList.contains('hidden')) {
            campoBuscaMobile.focus();
        }
    });

    campoBuscaMobile.addEventListener('input', () => {
        executarBusca(campoBuscaMobile.value.trim(), campoBuscaMobile, resultadosMobile);
    });

    document.addEventListener('click', (e) => {
        if (!buscaMobileContainer.contains(e.target) && !btnMobile.contains(e.target)) {
            resultadosMobile.classList.add('hidden');
        }
    });

})();