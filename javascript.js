
function calcularPlantas(largo, ancho, separacion) {
    // Paso 1. Calcular la cantidad de plántulas que se 
    // pueden sembrar a lo largo del terreno ( plantulasLargo : número entero )
    let plantulasLargo = ( largo / separacion ) + 1 ;

    // Paso 2. Calcular la cantidad de plántulas que se pueden sembrar a lo 
    // ancho del terreno ( plantulasAncho : número entero )
    let plantulasAncho = ( ancho / separacion ) + 1 ;

    // Paso 3. Calcular la cantidad total de plántulas que se pueden 
    // sembrar en el terreno ( cantidadPlantulas : número entero )
    let cantidadPlantulas = plantulasLargo * plantulasAncho ;

    return cantidadPlantulas ;
}

function calcularValorPagar(valorProducto) {
    let valorDescuento = 0 ;
    let valorPagar = 0 ;

    if (valorProducto < 20000) {
	    valorDescuento = valorProducto * 0.20 ;
    }
    else {
	    valorDescuento = valorProducto * 0.10 ;
    }
	
    valorPagar = valorProducto - valorDescuento ;

    return valorPagar ;
}
