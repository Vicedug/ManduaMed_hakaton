import React from 'react'

export function Header() {
    return (
        <header className="bg-white border-b border-gray-100 py-6 mb-8">
            <div className="container mx-auto px-4 flex justify-center items-center gap-3">
                <div className="w-10 h-10 rounded-full overflow-hidden flex-shrink-0">
                    <img
                        src="https://cdn.magicpatterns.com/uploads/inessdwLyiQvtK4MGSkEeo/Gemini_Generated_Image_e4bdm9e4bdm9e4bd-Photoroom.png"
                        alt="ManduadorMed Logo"
                        className="w-full h-full object-cover"
                    />
                </div>
                <h1 className="text-2xl font-bold tracking-tight">
                    <span className="text-[#2D5B6B]">Manduador</span>
                    <span className="text-[#4FB3A6]">Med</span>
                </h1>
            </div>
        </header>
    )
}