function cambioDP(monedas, total) {
  if (!Number.isSafeInteger(total) || total < 0 || total > 10000 ||
      !monedas.length || monedas.some(m => !Number.isSafeInteger(m) || m <= 0))
    throw new Error('Dominio invalido');
  monedas = [...new Set(monedas)].sort((a, b) => a - b);
  const dp = Array(total + 1).fill(total + 1),
        previo = Array(total + 1).fill(null);
  dp[0] = 0;
  for (let s = 1; s <= total; s++)
    for (const m of monedas) {
      if (m <= s && dp[s - m] + 1 < dp[s]) {
        dp[s] = dp[s - m] + 1;
        previo[s] = m;
      }
    }
  if (dp[total] === total + 1) return null;
  const resultado = [];
  while (total) {
    const m = previo[total];
    resultado.push(m);
    total -= m;
  }
  return resultado;
}
module.exports = {cambioDP};
if (require.main === module)
  console.log(JSON.stringify(cambioDP([1, 3, 4], 6)));
