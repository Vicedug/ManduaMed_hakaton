import React, { useState } from 'react'
import { Calendar, Trash2, ChevronDown } from 'lucide-react'

interface Medication {
  id: string
  name: string
  dose: string
  pending: number
  doses?: any[] // Added doses
}

type Props = {
  medications: Medication[]
  onDelete: (id: string) => void
}

export function MedicationCalendar({ medications, onDelete }: Props) {
  const [expandedId, setExpandedId] = useState<string | null>(null)
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
        {medications.map((med) => {
          const isExpanded = expandedId === med.id
          return (
            <div
              key={med.id}
              className="flex flex-col border-b border-gray-50 last:border-0"
            >
              <div className="flex flex-col sm:flex-row sm:items-center justify-between py-4 gap-4 sm:gap-0">
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
                    <button
                      onClick={() => onDelete(med.id)}
                      className="flex items-center gap-1.5 px-3 py-1.5 border border-red-300 text-red-500 rounded hover:bg-red-50 transition-colors text-sm"
                    >
                      <Trash2 className="w-4 h-4" />
                      <span>Eliminar Receta</span>
                    </button>
                    <button
                      onClick={() => setExpandedId(isExpanded ? null : med.id)}
                      className={`text-gray-400 hover:text-gray-600 transition-transform ${isExpanded ? 'rotate-180' : ''}`}
                    >
                      <ChevronDown className="w-5 h-5" />
                    </button>
                  </div>
                </div>
              </div>

              {isExpanded && med.doses && (
                <div className="bg-gray-50 p-4 rounded-lg mb-4 text-sm animate-in fade-in slide-in-from-top-2">
                  <h4 className="font-semibold text-gray-700 mb-2">Cronograma de Tomas:</h4>
                  <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                    {med.doses.map((dose: any, idx) => (
                      <div key={idx} className="bg-white p-2 rounded border border-gray-200 text-center">
                        <span className="block text-gray-500 text-xs">{dose.fecha}</span>
                        <span className="block font-medium text-[#2D5B6B]">{dose.hora}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )
        })}
      </div>
    </div>
  )
}