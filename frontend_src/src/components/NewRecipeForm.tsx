import React, { useState } from 'react'
import { Plus, Clock } from 'lucide-react'

type Props = {
    onAdd: (med: { name: string; dose: string; startTime: string; frequency: number; duration: number; notes: string }) => void
}

export function NewRecipeForm({ onAdd }: Props) {
    const [name, setName] = useState('')
    const [dose, setDose] = useState('')
    const [startTime, setStartTime] = useState('')
    const [frequency, setFrequency] = useState('')
    const [duration, setDuration] = useState('')
    const [notes, setNotes] = useState('')

    function submit(e) {
        e.preventDefault()
        if (!name) return

        onAdd({
            name,
            dose: dose || '1 dosis',
            startTime: startTime || '08:00',
            frequency: Number(frequency) || 8, // Default 8 seconds for demo
            duration: Number(duration) || 5, // Default 5 mins for demo
            notes
        })

        setName('')
        setDose('')
        setStartTime('')
        setFrequency('')
        setDuration('')
        setNotes('')
    }

    return (
        <div className="bg-white rounded-xl shadow-sm overflow-hidden h-fit">
            <div className="bg-[#2D5B6B] p-4 flex items-center gap-2 text-white">
                <Plus className="w-5 h-5" />
                <h2 className="font-medium text-lg">Nueva Receta</h2>
            </div>

            <form onSubmit={submit} className="p-6 space-y-5">
                <div>
                    <label className="block text-xs font-bold text-gray-600 uppercase mb-2">MEDICAMENTO</label>
                    <input value={name} onChange={(e) => setName(e.target.value)} type="text" placeholder="Ej: Paracetamol" className="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-gray-700" />
                </div>

                <div>
                    <label className="block text-xs font-bold text-gray-600 uppercase mb-2">DOSIS</label>
                    <input value={dose} onChange={(e) => setDose(e.target.value)} type="text" placeholder="Ej: 500mg" className="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-gray-700" />
                </div>

                <div>
                    <label className="block text-xs font-bold text-gray-600 uppercase mb-2">INICIAR A LAS (Hora 1ª Dosis)</label>
                    <div className="relative">
                        <input value={startTime} onChange={(e) => setStartTime(e.target.value)} type="time" placeholder="--:--" className="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-gray-700" />
                        <Clock className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
                    </div>
                </div>

                <div className="grid grid-cols-2 gap-4">
                    <div>
                        <label className="block text-xs font-bold text-gray-600 uppercase mb-2">CADA (Segundos)</label>
                        <input value={frequency} onChange={(e) => setFrequency(e.target.value)} type="number" placeholder="Ej: 8" className="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-gray-700" />
                    </div>
                    <div>
                        <label className="block text-xs font-bold text-gray-600 uppercase mb-2">DURANTE (Minutos)</label>
                        <input value={duration} onChange={(e) => setDuration(e.target.value)} type="number" placeholder="Ej: 5" className="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-gray-700" />
                    </div>
                </div>

                <div>
                    <label className="block text-xs font-bold text-gray-600 uppercase mb-2">NOTAS</label>
                    <textarea value={notes} onChange={(e) => setNotes(e.target.value)} placeholder="Opcional: Con comida..." rows={3} className="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-gray-700 resize-none" />
                </div>

                <button type="submit" className="w-full bg-[#6FB398] hover:bg-[#5da389] text-white font-medium py-3 rounded-lg transition-colors mt-2">Guardar Receta</button>
            </form>
        </div>
    )
}