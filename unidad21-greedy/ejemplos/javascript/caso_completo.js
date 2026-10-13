function cambioVoraz(monedas, total) {
  if (!Number.isSafeInteger(total) || total < 0 || total > 10000 ||
      !monedas.length || monedas.some(m => !Number.isSafeInteger(m) || m <= 0))
    throw new Error('Dominio invalido');
  const resultado = [];
  for (const m of [...new Set(monedas)].sort((a, b) => b - a)) {
    const cantidad = Math.floor(total / m);
    for (let i = 0; i < cantidad; i++) resultado.push(m);
    total %= m;
  }
  return total === 0 ? resultado : null;
}
module.exports = {cambioVoraz};
if (require.main === module)
  console.log(JSON.stringify(cambioVoraz([1, 3, 4], 6)));
