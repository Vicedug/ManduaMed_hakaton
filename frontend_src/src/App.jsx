import React, { useState, useEffect } from 'react'
import { Header } from './components/Header'
import { AlertConfig } from './components/AlertConfig'
import { NewRecipeForm } from './components/NewRecipeForm'
import { MedicationCalendar } from './components/MedicationCalendar'

export default function App() {
  const [medications, setMedications] = useState([])

  // Fetch medications from backend
  const fetchMedications = async () => {
    try {
      const response = await fetch('/api/recetas')
      if (response.ok) {
        const data = await response.json()
        setMedications(data)
      }
    } catch (error) {
      console.error('Error fetching medications:', error)
    }
  }

  useEffect(() => {
    fetchMedications()
  }, [])

  async function handleAdd(med) {
    try {
      // med contains: name, dose, startTime, frequency, duration, notes
      const response = await fetch('/api/recetas', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(med)
      })
      if (response.ok) {
        fetchMedications() // Refresh list
      }
    } catch (error) {
      console.error('Error adding medication:', error)
    }
  }

  async function handleDelete(id) {
    try {
      // id here is likely the group ID (e.g. "Paracetamol_500mg")
      const response = await fetch(`/api/recetas/${encodeURIComponent(id)}`, {
        method: 'DELETE'
      })
      if (response.ok) {
        fetchMedications()
      }
    } catch (error) {
      console.error('Error deleting medication:', error)
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 font-sans pb-12">
      <Header />
      <main className="container mx-auto px-4 max-w-6xl">
        <AlertConfig />
        <div className="grid grid-cols-1 lg:grid-cols-[380px_1fr] gap-8 items-start">
          <NewRecipeForm onAdd={handleAdd} />
          <MedicationCalendar medications={medications} onDelete={handleDelete} />
        </div>
      </main>
    </div>
  )
}