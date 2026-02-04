
const medications: Medication[] = [
    { id: '1', name: 'Prueba Demo 1', dose: '1 prueba', pending: 1 },
    { id: '2', name: 'Prueba Demo 2', dose: '1 prueba', pending: 1 },
    { id: '3', name: 'prueba1', dose: '1 pastilla', pending: 4 },
    { id: '4', name: 'ASPIRINA', dose: '1 pastilla', pending: 4 },
]

export function MedicationCalendar() {
    return (
        <div className="bg-white rounded-xl shadow-sm p-6 h-full">
            <div className="flex items-center gap-2 mb-6">
                <div className="text-orange-300">
                    <Calendar className="w-5 h-5" />
                </div>
                <h2 className="text-[#2D5B6B] font-bold text-lg">
                    Tu Calendario de Medicación
                </h2>
            </div>

            <div className="space-y-1">
                {medications.map((med) => (
                    <div
                        key={med.id}
                        className="flex flex-col sm:flex-row sm:items-center justify-between py-4 border-b border-gray-50 last:border-0 gap-4 sm:gap-0"
                    >
                        <div className="flex items-center gap-3">
                            <h3 className="font-bold text-gray-800 text-lg">{med.name}</h3>
                            <span className="bg-gray-100 text-gray-600 text-xs px-2 py-1 rounded-md font-medium">
                                {med.dose}
                            </span>
                        </div>

                        <div className="flex items-center justify-between sm:justify-end gap-4 w-full sm:w-auto">
                            <span className="text-gray-500 text-sm">
                                {med.pending} tomas pendientes
                            </span>

                            <div className="flex items-center gap-3">
                                <button className="flex items-center gap-1.5 px-3 py-1.5 border border-red-300 text-red-500 rounded hover:bg-red-50 transition-colors text-sm">
                                    <Trash2 className="w-4 h-4" />
                                    <span>Eliminar Receta</span>
                                </button>
                                <button className="text-gray-400 hover:text-gray-600">
                                    <ChevronDown className="w-5 h-5" />
                                </button>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}
