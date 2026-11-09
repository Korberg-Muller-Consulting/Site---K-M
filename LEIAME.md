# Site Korberg & Müller Consulting

Arquivos:
- `index.html`: o site completo (página única, sem servidor, sem chaves).
- `vercel.json`: cabeçalhos de segurança para a Vercel.
- `_headers`: os mesmos cabeçalhos para Cloudflare Pages ou Netlify.

## Antes de publicar, preencha
- `Felipe [SOBRENOME]` e `Mariana [SOBRENOME]`, as duas mini-bios e as fotos (seção Liderança).
- `[contato@seudominio.com.br]`: aparece no texto da seção Contato e na variável `CONTACT_EMAIL` dentro do `<script>`.
- `[CNPJ ...]` no rodapé.

Importante: o cabeçalho de segurança (CSP) autoriza apenas o script atual, pela "impressão digital" (hash). Se o conteúdo do `<script>` mudar (por exemplo, ao trocar o e-mail), o hash precisa ser recalculado no `vercel.json` e no `_headers`. Peça ao Claude para fazer isso junto com a alteração.

## Publicar grátis na Vercel (recomendado, vocês já usam)
1. Crie um repositório no GitHub (ex.: `km-site`) e envie estes arquivos.
2. Em vercel.com, Add New › Project › importe o repositório › Deploy (sem configuração extra).
3. O site fica em `km-site.vercel.app`. Cada novo envio ao GitHub atualiza o site sozinho.

## Alternativas também gratuitas
- Cloudflare Pages: Workers & Pages › Create › Pages › conectar o GitHub ou arrastar a pasta.
- Netlify: arrastar a pasta em app.netlify.com/drop.
- GitHub Pages: Settings › Pages do repositório (não aplica os cabeçalhos de segurança).

## Domínio próprio
O endereço `.vercel.app` é gratuito. Para `korbergmuller.com.br`, registre no Registro.br (pago, anual) e aponte o DNS em Vercel › Settings › Domains. O HTTPS é automático e gratuito.
