import React, { useState } from 'react'
import { Settings, Info, Send } from 'lucide-react'

export function AlertConfig() {
  const [token, setToken] = useState('8191416458:AAHu3u_2nl6nvtsl54FcOMMii_m5o_yf4yM')
  const [chatId, setChatId] = useState('5909499186')

  // load saved config
  React.useEffect(() => {
    const saved = localStorage.getItem('alertConfig')
    if (saved) {
      try {
        const parsed = JSON.parse(saved)
        if (parsed.token) setToken(parsed.token)
        if (parsed.chatId) setChatId(parsed.chatId)
      } catch {}
    }
  }, [])

  function save() {
    localStorage.setItem('alertConfig', JSON.stringify({ token, chatId }))
    alert('Configuración guardada')
  }

  return (
    <div className="bg-white rounded-xl shadow-sm p-6 mb-8">
      <div className="flex items-center gap-2 mb-4 text-gray-700">
        <Settings className="w-5 h-5 text-purple-400" />
        <h2 className="text-lg font-medium text-gray-600">
          Configuración de Alertas
        </h2>
      </div>

      <div className="bg-[#E0F7FA] border border-blue-100 rounded-lg p-4 mb-6 flex items-start gap-3">
        <Info className="w-5 h-5 text-blue-500 flex-shrink-0 mt-0.5" />
        <p className="text-sm text-gray-700">
          Configura tu <span className="font-semibold">Telegram Bot</span> para
          recibir alertas en el celular sin abrir el navegador.
        </p>
      </div>

      <div className="space-y-4">
        <div className="flex items-center gap-2 mb-2">
          <Send className="w-4 h-4 text-blue-400" />
          <span className="text-sm font-medium text-blue-400">Telegram Bot</span>
        </div>

        <div className="flex flex-col sm:flex-row rounded-md overflow-hidden border border-gray-200">
          <div className="bg-gray-50 px-4 py-2 border-b sm:border-b-0 sm:border-r border-gray-200 min-w-[100px] flex items-center text-gray-600 text-sm font-medium">
            Token
          </div>
          <input
            type="text"
            value={token}
            onChange={(e) => setToken(e.target.value)}
            className="flex-1 px-4 py-2 outline-none text-gray-800 text-sm w-full"
            placeholder="Enter bot token"
          />
        </div>

        <div className="flex flex-col sm:flex-row rounded-md overflow-hidden border border-gray-200">
          <div className="bg-gray-50 px-4 py-2 border-b sm:border-b-0 sm:border-r border-gray-200 min-w-[100px] flex items-center text-gray-600 text-sm font-medium">
            Chat ID
          </div>
          <input
            type="text"
            value={chatId}
            onChange={(e) => setChatId(e.target.value)}
            className="flex-1 px-4 py-2 outline-none text-gray-800 text-sm w-full"
            placeholder="Enter chat ID"
          />
        </div>

        <div className="flex justify-end mt-4">
          <button onClick={save} className="px-6 py-2 border border-blue-400 text-blue-500 rounded-md hover:bg-blue-50 transition-colors text-sm font-medium">
            Guardar Configuración
          </button>
        </div>
      </div>
    </div>
  )
}
