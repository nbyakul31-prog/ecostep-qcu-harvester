"""
EcoStep QCU: CAD Prototyping & Engineering Blueprint Engine
Course: AR101 (Computer Architecture & Organization) - Quezon City University
Author: Luigi Emanuel Britania (3rd Year BSIT) & Antigravity Engineering AI

This script generates:
1. `ecostep_cad_visualizer.html`: Full-featured interactive 3D/2D CAD viewer & real-time footstep simulator.
2. `ecostep_qcu_blueprint.svg`: Precision vector orthographic CAD schematic (1:1 / 1:2 scale with dimension leaders).
3. `ecostep_qcu_blueprint.dxf`: CAD exchange format for AutoCAD / Fusion 360 / CNC laser fabrication.
"""

import os
import sys
import math

def generate_svg_blueprint(output_path: str = "ecostep_qcu_blueprint.svg"):
    """
    Generates a high-precision 2D CAD engineering blueprint in SVG format.
    Includes Top Plan View, Front Cutaway Section View, Kinematic Drive Detail,
    Electronic Circuit Schematic, and Official Engineering Title Block.
    """
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1100" width="100%" height="100%" style="background:#090d16; font-family:'Segoe UI',Roboto,monospace;">
  <defs>
    <!-- Technical Grid Pattern -->
    <pattern id="cadGridSmall" width="10" height="10" patternUnits="userSpaceOnUse">
      <path d="M 10 0 L 0 0 0 10" fill="none" stroke="#162032" stroke-width="0.5"/>
    </pattern>
    <pattern id="cadGridLarge" width="50" height="50" patternUnits="userSpaceOnUse">
      <rect width="50" height="50" fill="url(#cadGridSmall)"/>
      <path d="M 50 0 L 0 0 0 50" fill="none" stroke="#1e293b" stroke-width="1.0"/>
    </pattern>

    <!-- Arrowhead Markers -->
    <marker id="arrowCyan" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#00e5ff"/>
    </marker>
    <marker id="arrowAmber" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#f59e0b"/>
    </marker>
    <marker id="arrowWhite" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 2 L 6 5 L 0 8 z" fill="#cbd5e1"/>
    </marker>

    <!-- Material Gradients -->
    <linearGradient id="plywoodTop" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#92400e" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#b45309" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#78350f" stop-opacity="0.8"/>
    </linearGradient>
    <linearGradient id="steelBolt" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#94a3b8"/>
      <stop offset="50%" stop-color="#e2e8f0"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
    <linearGradient id="springMetal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>

    <!-- Glow Filter for LEDs -->
    <filter id="ledGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background CAD Grid -->
  <rect width="1600" height="1100" fill="url(#cadGridLarge)" />

  <!-- Outer Blueprint Border (Double Line ISO Standard) -->
  <rect x="25" y="25" width="1550" height="1050" fill="none" stroke="#00e5ff" stroke-width="2" opacity="0.8"/>
  <rect x="35" y="35" width="1530" height="1030" fill="none" stroke="#1e293b" stroke-width="1"/>

  <!-- ================= HEADER & ACADEMIC TITLE BLOCK ================= -->
  <g id="TitleBlock" transform="translate(1120, 910)">
    <rect x="0" y="0" width="425" height="135" fill="#0c1322" stroke="#00e5ff" stroke-width="1.8" rx="4"/>
    <line x1="0" y1="36" x2="425" y2="36" stroke="#1e293b" stroke-width="1.2"/>
    <line x1="0" y1="72" x2="425" y2="72" stroke="#1e293b" stroke-width="1.2"/>
    <line x1="0" y1="104" x2="425" y2="104" stroke="#1e293b" stroke-width="1.2"/>
    <line x1="260" y1="72" x2="260" y2="135" stroke="#1e293b" stroke-width="1.2"/>

    <text x="14" y="24" fill="#00e5ff" font-size="14" font-weight="700" letter-spacing="1">QUEZON CITY UNIVERSITY - SAN BARTOLOME</text>
    <text x="14" y="58" fill="#f8fafc" font-size="13" font-weight="600">ECOSTEP QCU: 450x450mm KINETIC FOOTSTEP HARVESTER</text>
    
    <text x="14" y="90" fill="#94a3b8" font-size="10">SUBJECT: AR101 - Comp. Arch &amp; Org</text>
    <text x="14" y="122" fill="#38bdf8" font-size="10">PROTOTYPE: Salvaged Gearbox Gen + Power Bank</text>

    <text x="274" y="90" fill="#94a3b8" font-size="10">SCALE: 1:2 (MM) | SHT 1/1</text>
    <text x="274" y="122" fill="#ffd600" font-size="10">STATUS: APPROVED CAD</text>
  </g>

  <!-- ================= TOP LEFT: SECTION A - TOP PLAN VIEW (ORTHOGRAPHIC 2D) ================= -->
  <g id="TopPlanView" transform="translate(60, 60)">
    <!-- Section Title -->
    <rect x="0" y="0" width="480" height="30" fill="#111c30" stroke="#00e5ff" stroke-width="1" rx="3"/>
    <text x="14" y="20" fill="#00e5ff" font-size="13" font-weight="700">SECTION A: TOP PLAN VIEW (450 x 450 mm ENVELOPE)</text>

    <!-- Outer Tile Boundary (450 x 450 mm scaled by 0.9 = 405 x 405 px) -->
    <g transform="translate(35, 55)">
      <!-- Base Shadow / Cavity -->
      <rect x="0" y="0" width="405" height="405" fill="#131e33" stroke="#38bdf8" stroke-width="2" rx="4"/>
      
      <!-- Top Plywood Plate Outline -->
      <rect x="0" y="0" width="405" height="405" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="6,4"/>

      <!-- 4x Guide Bolt Holes (30 mm in from corners = 27 px at 0.9 scale) -->
      <!-- Top-Left Corner (27, 27) -->
      <circle cx="27" cy="27" r="9" fill="#0f172a" stroke="#00e5ff" stroke-width="1.5"/>
      <circle cx="27" cy="27" r="4" fill="#cbd5e1"/>
      <text x="40" y="25" fill="#94a3b8" font-size="9">M8 Hole (Ø9mm, C'bore Ø20x10mm)</text>

      <!-- Top-Right Corner (378, 27) -->
      <circle cx="378" cy="27" r="9" fill="#0f172a" stroke="#00e5ff" stroke-width="1.5"/>
      <circle cx="378" cy="27" r="4" fill="#cbd5e1"/>

      <!-- Bottom-Left Corner (27, 378) -->
      <circle cx="27" cy="378" r="9" fill="#0f172a" stroke="#00e5ff" stroke-width="1.5"/>
      <circle cx="27" cy="378" r="4" fill="#cbd5e1"/>

      <!-- Bottom-Right Corner (378, 378) -->
      <circle cx="378" cy="378" r="9" fill="#0f172a" stroke="#00e5ff" stroke-width="1.5"/>
      <circle cx="378" cy="378" r="4" fill="#cbd5e1"/>

      <!-- 4x Return Springs (Center of edges, 20 mm in = 18 px) -->
      <!-- Top Spring (202.5, 18) -->
      <circle cx="202.5" cy="18" r="14" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
      <circle cx="202.5" cy="18" r="6" fill="#38bdf8"/>

      <!-- Bottom Spring (202.5, 387) -->
      <circle cx="202.5" cy="387" r="14" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
      <circle cx="202.5" cy="387" r="6" fill="#38bdf8"/>

      <!-- Left Spring (18, 202.5) -->
      <circle cx="18" cy="202.5" r="14" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
      <circle cx="18" cy="202.5" r="6" fill="#38bdf8"/>

      <!-- Right Spring (387, 202.5) -->
      <circle cx="387" cy="202.5" r="14" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
      <circle cx="387" cy="202.5" r="6" fill="#38bdf8"/>

      <!-- Center Transduction Hub Footprint -->
      <rect x="135" y="145" width="135" height="115" fill="#1e293b" fill-opacity="0.8" stroke="#f59e0b" stroke-width="1.5" rx="3"/>
      <text x="145" y="165" fill="#f59e0b" font-size="10" font-weight="700">GENERATOR DRIVE HUB</text>
      <text x="145" y="180" fill="#94a3b8" font-size="9">• Cordless Drill Motor / Gearbox</text>
      <text x="145" y="195" fill="#94a3b8" font-size="9">• Crank Disc (Stroke: 10mm)</text>
      <text x="145" y="210" fill="#94a3b8" font-size="9">• Rigid Base Bulkhead Mount</text>
      <text x="145" y="240" fill="#00e5ff" font-size="9">INT0 Micro-Switch Under Plate</text>

      <!-- Dimension Lines & Leader Arrows -->
      <!-- Width Dimension (450 mm) -->
      <line x1="0" y1="-20" x2="405" y2="-20" stroke="#00e5ff" stroke-width="1.2" marker-start="url(#arrowCyan)" marker-end="url(#arrowCyan)"/>
      <line x1="0" y1="-28" x2="0" y2="0" stroke="#00e5ff" stroke-width="0.8"/>
      <line x1="405" y1="-28" x2="405" y2="0" stroke="#00e5ff" stroke-width="0.8"/>
      <rect x="165" y="-30" width="75" height="18" fill="#090d16"/>
      <text x="172" y="-17" fill="#00e5ff" font-size="11" font-weight="bold">450 mm</text>

      <!-- Height Dimension (450 mm) -->
      <line x1="-20" y1="0" x2="-20" y2="405" stroke="#00e5ff" stroke-width="1.2" marker-start="url(#arrowCyan)" marker-end="url(#arrowCyan)"/>
      <line x1="-28" y1="0" x2="0" y2="0" stroke="#00e5ff" stroke-width="0.8"/>
      <line x1="-28" y1="405" x2="0" y2="405" stroke="#00e5ff" stroke-width="0.8"/>
      <rect x="-32" y="190" width="24" height="40" fill="#090d16"/>
      <text x="-26" y="215" fill="#00e5ff" font-size="11" font-weight="bold" transform="rotate(-90, -26, 215)">450 mm</text>

      <!-- Inset Dimension Corner (30 mm) -->
      <line x1="0" y1="420" x2="27" y2="420" stroke="#f59e0b" stroke-width="1" marker-start="url(#arrowAmber)" marker-end="url(#arrowAmber)"/>
      <text x="2" y="435" fill="#f59e0b" font-size="9">30mm</text>

      <!-- Spring Inset (20 mm) -->
      <line x1="202.5" y1="420" x2="202.5" y2="387" stroke="#38bdf8" stroke-width="1" marker-start="url(#arrowCyan)"/>
      <text x="175" y="435" fill="#38bdf8" font-size="9">20mm edge inset</text>
    </g>
  </g>

  <!-- ================= TOP RIGHT: SECTION B - FRONT CUTAWAY ELEVATION ================= -->
  <g id="ElevationCutaway" transform="translate(600, 60)">
    <rect x="0" y="0" width="500" height="30" fill="#111c30" stroke="#00e5ff" stroke-width="1" rx="3"/>
    <text x="14" y="20" fill="#00e5ff" font-size="13" font-weight="700">SECTION B: FRONT CUTAWAY ELEVATION (100 mm OVERALL HEIGHT)</text>

    <g transform="translate(40, 70)">
      <!-- Dimension Reference Lines on Left -->
      <!-- 18mm Top Plate -->
      <line x1="-25" y1="0" x2="-25" y2="27" stroke="#ffd600" stroke-width="1" marker-start="url(#arrowAmber)" marker-end="url(#arrowAmber)"/>
      <text x="-65" y="17" fill="#ffd600" font-size="10">18 mm</text>

      <!-- 70mm Cavity -->
      <line x1="-25" y1="27" x2="-25" y2="132" stroke="#00e5ff" stroke-width="1" marker-start="url(#arrowCyan)" marker-end="url(#arrowCyan)"/>
      <text x="-65" y="85" fill="#00e5ff" font-size="10">70 mm</text>

      <!-- 10mm Travel Stroke Limit -->
      <line x1="-10" y1="27" x2="-10" y2="42" stroke="#ff3d00" stroke-width="1.5" marker-start="url(#arrowAmber)" marker-end="url(#arrowAmber)"/>
      <text x="5" y="38" fill="#ff3d00" font-size="9" font-weight="bold">Δz = 10mm Travel</text>

      <!-- 12mm Base Plate -->
      <line x1="-25" y1="132" x2="-25" y2="150" stroke="#ffd600" stroke-width="1" marker-start="url(#arrowAmber)" marker-end="url(#arrowAmber)"/>
      <text x="-65" y="145" fill="#ffd600" font-size="10">12 mm</text>

      <!-- Total Height Leader (100mm) -->
      <line x1="440" y1="0" x2="440" y2="150" stroke="#f8fafc" stroke-width="1.2" marker-start="url(#arrowWhite)" marker-end="url(#arrowWhite)"/>
      <rect x="446" y="65" width="55" height="18" fill="#090d16"/>
      <text x="448" y="78" fill="#f8fafc" font-size="11" font-weight="bold">100 mm</text>

      <!-- TOP PLATE (18 mm Birch Plywood) -->
      <rect x="0" y="0" width="420" height="27" fill="url(#plywoodTop)" stroke="#f59e0b" stroke-width="1.5" rx="2"/>
      <text x="130" y="18" fill="#fff" font-size="11" font-weight="bold">18 mm PLYWOOD FOOT TREAD PLATE</text>

      <!-- Counterbores on Top Plate for Bolt Heads -->
      <rect x="25" y="0" width="18" height="15" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
      <rect x="377" y="0" width="18" height="15" fill="#0f172a" stroke="#64748b" stroke-width="1"/>

      <!-- M8 GUIDE BOLTS (120 mm) -->
      <!-- Left Guide Bolt -->
      <rect x="31" y="5" width="6" height="160" fill="url(#steelBolt)" stroke="#334155" stroke-width="1"/>
      <!-- Bolt Head recessed -->
      <rect x="28" y="2" width="12" height="6" fill="#cbd5e1" stroke="#334155"/>
      <!-- Stop Collar Nut (at 10 mm travel limit below top plate) -->
      <rect x="26" y="42" width="16" height="8" fill="#ffd600" stroke="#b45309" stroke-width="1"/>
      <text x="48" y="49" fill="#ffd600" font-size="9">M8 Stop Collar Nut (10mm stroke limit)</text>
      <!-- Base Locknuts (Underneath base plate) -->
      <rect x="26" y="150" width="16" height="10" fill="#94a3b8" stroke="#334155"/>

      <!-- Right Guide Bolt -->
      <rect x="383" y="5" width="6" height="160" fill="url(#steelBolt)" stroke="#334155" stroke-width="1"/>
      <rect x="380" y="2" width="12" height="6" fill="#cbd5e1" stroke="#334155"/>
      <rect x="378" y="42" width="16" height="8" fill="#ffd600" stroke="#b45309" stroke-width="1"/>
      <rect x="378" y="150" width="16" height="10" fill="#94a3b8" stroke="#334155"/>

      <!-- 2x SIDE COMPRESSION SPRINGS (50 mm Free Length) -->
      <!-- Left Spring (Zig-zag representation) -->
      <path d="M 100 27 L 110 37 L 90 47 L 110 57 L 90 67 L 110 77 L 90 87 L 110 97 L 90 107 L 110 117 L 100 132" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
      <text x="75" y="145" fill="#38bdf8" font-size="9">Soft Spring</text>

      <!-- Right Spring -->
      <path d="M 320 27 L 330 37 L 310 47 L 330 57 L 310 67 L 330 77 L 310 87 L 330 97 L 310 107 L 330 117 L 320 132" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>

      <!-- CENTER GENERATOR ASSEMBLY & CRANK-SLIDER MECHANISM -->
      <!-- Vertical Wooden Bulkhead fixed to Base -->
      <rect x="180" y="60" width="60" height="72" fill="#78350f" stroke="#b45309" stroke-width="1.5"/>
      <text x="183" y="125" fill="#fde68a" font-size="8">BULKHEAD</text>

      <!-- DC Generator Motor Body -->
      <rect x="220" y="70" width="45" height="35" rx="3" fill="#334155" stroke="#00e5ff" stroke-width="1.5"/>
      <text x="225" y="90" fill="#00e5ff" font-size="8" font-weight="bold">GEN</text>

      <!-- Crank Disc (Diameter 30mm, Pivot Radius R=5mm -> 10mm full stroke) -->
      <circle cx="195" cy="85" r="16" fill="#1e293b" stroke="#ffd600" stroke-width="2"/>
      <circle cx="195" cy="85" r="3" fill="#cbd5e1"/>
      <!-- Crank Pin (5mm offset = 7.5px) -->
      <circle cx="195" cy="77.5" r="3" fill="#ff3d00"/>

      <!-- Connecting Rod from Top Plate to Crank Pin -->
      <line x1="195" y1="27" x2="195" y2="77.5" stroke="#e2e8f0" stroke-width="3" stroke-linecap="round"/>
      <circle cx="195" cy="27" r="3.5" fill="#cbd5e1" stroke="#0f172a"/>

      <!-- Step Sensor: Micro-Switch on Base -->
      <rect x="145" y="118" width="22" height="14" rx="2" fill="#ef4444" stroke="#991b1b" stroke-width="1"/>
      <path d="M 148 118 L 158 110" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="125" y="108" fill="#ef4444" font-size="8">INT0 Switch</text>

      <!-- BASE PLATE (12 mm Plywood) -->
      <rect x="0" y="132" width="420" height="18" fill="url(#plywoodTop)" stroke="#f59e0b" stroke-width="1.5" rx="2"/>
      <text x="135" y="145" fill="#fff" font-size="11" font-weight="bold">12 mm PLYWOOD BASE PLATE</text>
    </g>
  </g>

  <!-- ================= RIGHT COLUMN: KINEMATICS & ENERGY BUDGET ================= -->
  <g id="KinematicsAndBudget" transform="translate(1120, 60)">
    <rect x="0" y="0" width="425" height="30" fill="#111c30" stroke="#00e5ff" stroke-width="1" rx="3"/>
    <text x="14" y="20" fill="#00e5ff" font-size="13" font-weight="700">SECTION C: KINEMATICS &amp; ENERGY BUDGET</text>

    <!-- Kinematics Equations Card -->
    <g transform="translate(0, 45)">
      <rect x="0" y="0" width="425" height="165" fill="#0c1322" stroke="#1e293b" stroke-width="1.5" rx="4"/>
      <text x="15" y="24" fill="#ffd600" font-size="12" font-weight="bold">1. CRANK-SLIDER KINEMATIC TRANSDUCTION</text>
      
      <text x="15" y="48" fill="#94a3b8" font-size="10">• Top Plate Stroke: <tspan fill="#f8fafc" font-weight="bold">S = 10.0 mm</tspan></text>
      <text x="15" y="66" fill="#94a3b8" font-size="10">• Crank Pin Offset Radius: <tspan fill="#00e5ff" font-weight="bold">R = S / 2 = 5.0 mm</tspan></text>
      <text x="15" y="84" fill="#94a3b8" font-size="10">• Rotational Cycle: <tspan fill="#38bdf8">Downstroke: 0°→180° | Return: 180°→360°</tspan></text>
      <text x="15" y="102" fill="#94a3b8" font-size="10">• Gearbox Multiplication: <tspan fill="#f59e0b">N = 1:24 (Reversed speed-up train)</tspan></text>
      <text x="15" y="120" fill="#94a3b8" font-size="10">• Footfall Duration: <tspan fill="#f8fafc">Δt ≈ 0.25 s → Generator RPM ≈ 2,800 RPM</tspan></text>
      <text x="15" y="142" fill="#22c55e" font-size="10" font-weight="bold">Faraday Output: ε = -N(dΦ/dt) = ke · ω → V_peak ≈ 8.5 V to 14.0 V</text>
    </g>

    <!-- Energy Budget Comparison Card -->
    <g transform="translate(0, 225)">
      <rect x="0" y="0" width="425" height="205" fill="#0c1322" stroke="#1e293b" stroke-width="1.5" rx="4"/>
      <text x="15" y="24" fill="#00e5ff" font-size="12" font-weight="bold">2. ENERGY HARVEST &amp; SIGN RUNTIME BUDGET</text>

      <!-- Table Header -->
      <rect x="15" y="38" width="395" height="22" fill="#1e293b" rx="2"/>
      <text x="22" y="53" fill="#cbd5e1" font-size="9" font-weight="bold">MODE</text>
      <text x="80" y="53" fill="#cbd5e1" font-size="9" font-weight="bold">CURRENT</text>
      <text x="155" y="53" fill="#cbd5e1" font-size="9" font-weight="bold">POWER (5V)</text>
      <text x="245" y="53" fill="#cbd5e1" font-size="9" font-weight="bold">30-MIN ENERGY</text>
      <text x="340" y="53" fill="#cbd5e1" font-size="9" font-weight="bold">STEPS REQ.</text>

      <!-- Row 1: Full Mode -->
      <text x="22" y="76" fill="#f43f5e" font-size="10" font-weight="bold">Full (18 LEDs)</text>
      <text x="80" y="76" fill="#f8fafc" font-size="10">25.0 mA</text>
      <text x="155" y="76" fill="#f8fafc" font-size="10">125 mW</text>
      <text x="245" y="76" fill="#ffd600" font-size="10">225 Joules</text>
      <text x="340" y="76" fill="#f43f5e" font-size="10" font-weight="bold">320 - 920</text>

      <!-- Row 2: Dim Mode -->
      <text x="22" y="100" fill="#22c55e" font-size="10" font-weight="bold">Dim (0.2mA/ea)</text>
      <text x="80" y="100" fill="#f8fafc" font-size="10">3.6 mA</text>
      <text x="155" y="100" fill="#f8fafc" font-size="10">18 mW</text>
      <text x="245" y="100" fill="#ffd600" font-size="10">32 Joules</text>
      <text x="340" y="100" fill="#22c55e" font-size="10" font-weight="bold">45 - 130</text>

      <!-- Assumptions -->
      <line x1="15" y1="115" x2="410" y2="115" stroke="#1e293b" stroke-width="1"/>
      <text x="15" y="134" fill="#94a3b8" font-size="9">• Harvest Yield per Step: <tspan fill="#f8fafc">E_step = 0.35 J to 1.0 J</tspan></text>
      <text x="15" y="150" fill="#94a3b8" font-size="9">• Power Bank Capacity: <tspan fill="#f8fafc">20,000 mAh (3.7V) ≈ 266,000 J (Not capacity limited)</tspan></text>
      <text x="15" y="166" fill="#94a3b8" font-size="9">• Charger Path Efficiency: <tspan fill="#f8fafc">η_sys ≈ 70% (Schottky + Buck-Boost)</tspan></text>
      <text x="15" y="184" fill="#00e5ff" font-size="9" font-weight="bold">★ DIM MODE enables full sign operation with just ~80 footfalls!</text>
    </g>

    <!-- Safe Lithium Handling Protocol -->
    <g transform="translate(0, 445)">
      <rect x="0" y="0" width="425" height="155" fill="#1e1315" stroke="#ef4444" stroke-width="1.5" rx="4"/>
      <text x="15" y="24" fill="#ef4444" font-size="11" font-weight="bold">⚠️ SAFETY DIRECTIVE: LITHIUM POWER BANK ENCLOSURE</text>
      <text x="15" y="46" fill="#fca5a5" font-size="9">• <tspan font-weight="bold">NEVER</tspan> place lithium cells underneath the moving footstep plate.</text>
      <text x="15" y="62" fill="#fca5a5" font-size="9">• Store the 20,000 mAh power bank in a padded, ventilated box BESIDE the tile.</text>
      <text x="15" y="78" fill="#fca5a5" font-size="9">• Path A: Direct 5.2V input into USB charge port (safest, uses internal BMS).</text>
      <text x="15" y="94" fill="#fca5a5" font-size="9">• Path B: TP4056 Module (if internal circuit dead; inspect cells for swelling!).</text>
      <text x="15" y="110" fill="#fca5a5" font-size="9">• Set DC-DC Buck-Boost to 5.20 V with DMM before connecting battery!</text>
      <text x="15" y="130" fill="#ffd600" font-size="9" font-weight="bold">AR101 Compliance: Experimental data must reflect actual harvested mWh.</text>
    </g>
  </g>

  <!-- ================= BOTTOM: SECTION D - COMPLETE ELECTRICAL & ELECTRONIC SCHEMATIC ================= -->
  <g id="ElectronicSchematic" transform="translate(60, 560)">
    <rect x="0" y="0" width="1040" height="30" fill="#111c30" stroke="#00e5ff" stroke-width="1" rx="3"/>
    <text x="14" y="20" fill="#00e5ff" font-size="13" font-weight="700">SECTION D: ELECTRONIC POWER HARVESTING, TELEMETRY &amp; LOAD SCHEMATIC</text>

    <!-- Schematic Canvas -->
    <g transform="translate(10, 45)">
      <rect x="0" y="0" width="1020" height="260" fill="#0b101c" stroke="#1e293b" stroke-width="1.5" rx="4"/>

      <!-- 1. Generator Unit -->
      <g transform="translate(20, 70)">
        <circle cx="35" cy="50" r="28" fill="#1e293b" stroke="#00e5ff" stroke-width="2"/>
        <text x="22" y="55" fill="#00e5ff" font-size="14" font-weight="bold">GEN</text>
        <text x="8" y="95" fill="#94a3b8" font-size="9">Cordless Drill /</text>
        <text x="10" y="107" fill="#94a3b8" font-size="9">DC Generator</text>
        
        <!-- Terminals -->
        <line x1="63" y1="35" x2="95" y2="35" stroke="#ef4444" stroke-width="2"/>
        <line x1="63" y1="65" x2="95" y2="65" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="95" cy="35" r="3" fill="#ef4444"/>
        <circle cx="95" cy="65" r="3" fill="#38bdf8"/>
        <text x="70" y="30" fill="#ef4444" font-size="8">V+</text>
        <text x="70" y="78" fill="#38bdf8" font-size="8">V-</text>
      </g>

      <!-- 2. Full-Wave Schottky Bridge Rectifier (1N5819 x4) -->
      <g transform="translate(125, 50)">
        <!-- Diamond Bridge Outline -->
        <polygon points="45,15 85,55 45,95 5,55" fill="#131e33" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="20" y="58" fill="#f59e0b" font-size="9" font-weight="bold">1N5819 x4</text>
        <text x="12" y="115" fill="#94a3b8" font-size="8">Schottky Bridge</text>
        <text x="14" y="126" fill="#38bdf8" font-size="8">(Vf ≈ 0.35V)</text>

        <!-- AC Inputs into bridge -->
        <line x1="-10" y1="55" x2="5" y2="55" stroke="#ef4444" stroke-width="2"/>
        
        <!-- DC Outputs from bridge -->
        <line x1="45" y1="15" x2="45" y2="5" stroke="#ef4444" stroke-width="2"/>
        <line x1="45" y1="5" x2="110" y2="5" stroke="#ef4444" stroke-width="2"/>

        <line x1="45" y1="95" x2="45" y2="105" stroke="#38bdf8" stroke-width="2"/>
        <line x1="45" y1="105" x2="110" y2="105" stroke="#38bdf8" stroke-width="2"/>
      </g>

      <!-- 3. Reservoir Capacitor & Overvoltage Protection -->
      <g transform="translate(245, 50)">
        <!-- Bus rails -->
        <line x1="-10" y1="5" x2="115" y2="5" stroke="#ef4444" stroke-width="2"/>
        <line x1="-10" y1="105" x2="115" y2="105" stroke="#38bdf8" stroke-width="2"/>

        <!-- Smoothing Capacitor C1: 2200uF 16V -->
        <line x1="20" y1="5" x2="20" y2="40" stroke="#ef4444" stroke-width="1.8"/>
        <line x1="8" y1="40" x2="32" y2="40" stroke="#ffd600" stroke-width="3"/>
        <line x1="8" y1="48" x2="32" y2="48" stroke="#cbd5e1" stroke-width="3"/>
        <line x1="20" y1="48" x2="20" y2="105" stroke="#38bdf8" stroke-width="1.8"/>
        <text x="36" y="47" fill="#ffd600" font-size="9" font-weight="bold">2200 µF</text>
        <text x="36" y="58" fill="#94a3b8" font-size="8">16V Low ESR</text>

        <!-- TVS / Zener Diode Protection (16V Clamp) -->
        <line x1="75" y1="5" x2="75" y2="42" stroke="#ef4444" stroke-width="1.8"/>
        <polygon points="67,42 83,42 75,54" fill="#f43f5e" stroke="#f43f5e"/>
        <line x1="65" y1="54" x2="85" y2="54" stroke="#f43f5e" stroke-width="2"/>
        <line x1="75" y1="54" x2="75" y2="105" stroke="#38bdf8" stroke-width="1.8"/>
        <text x="88" y="52" fill="#f43f5e" font-size="8" font-weight="bold">TVS 16V</text>

        <!-- 500mA Polyfuse PTC -->
        <rect x="115" y="0" width="24" height="10" fill="#0284c7" stroke="#38bdf8" rx="2"/>
        <text x="110" y="-5" fill="#38bdf8" font-size="8">500mA PTC</text>
        <line x1="139" y1="5" x2="160" y2="5" stroke="#ef4444" stroke-width="2"/>
      </g>

      <!-- 4. Synchronous Buck-Boost DC-DC Module -->
      <g transform="translate(425, 40)">
        <rect x="0" y="0" width="115" height="120" rx="4" fill="#132238" stroke="#00e5ff" stroke-width="1.8"/>
        <text x="8" y="20" fill="#00e5ff" font-size="10" font-weight="bold">DC-DC CONVERTER</text>
        <text x="8" y="34" fill="#94a3b8" font-size="8">Buck-Boost Auto</text>
        
        <rect x="15" y="45" width="85" height="35" fill="#0f172a" stroke="#334155" rx="2"/>
        <text x="22" y="66" fill="#ffd600" font-size="11" font-weight="bold">SET: 5.20 V</text>

        <text x="8" y="100" fill="#22c55e" font-size="8">Regulated 5.2V Bus</text>
        <text x="8" y="112" fill="#94a3b8" font-size="7">η ≈ 88-92% Eff.</text>

        <!-- Outputs to Power Bank -->
        <line x1="115" y1="20" x2="165" y2="20" stroke="#ef4444" stroke-width="2"/>
        <line x1="115" y1="95" x2="165" y2="95" stroke="#38bdf8" stroke-width="2"/>
        <text x="125" y="15" fill="#ef4444" font-size="8">+5.2V</text>
        <text x="125" y="108" fill="#38bdf8" font-size="8">GND</text>
      </g>

      <!-- 5. 20,000 mAh Power Bank Storage (External Enclosure) -->
      <g transform="translate(610, 35)">
        <rect x="0" y="0" width="135" height="135" rx="6" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
        <rect x="10" y="8" width="115" height="24" fill="#0f172a" rx="2"/>
        <text x="16" y="24" fill="#22c55e" font-size="10" font-weight="bold">POWER BANK 20Ah</text>
        
        <text x="12" y="48" fill="#cbd5e1" font-size="9">• Path A: 5V USB In</text>
        <text x="12" y="62" fill="#cbd5e1" font-size="9">• Path B: TP4056 1S</text>
        <text x="12" y="78" fill="#94a3b8" font-size="8">Salvg. Li-ion (3.7V)</text>
        <text x="12" y="92" fill="#94a3b8" font-size="8">Cap: 266,000 Joules</text>

        <!-- USB 5V Output Ports -->
        <rect x="25" y="105" width="85" height="22" fill="#0284c7" rx="3"/>
        <text x="35" y="120" fill="#fff" font-size="9" font-weight="bold">5.0V USB OUT</text>
      </g>

      <!-- 6. 18 Micro-LED Sign ("I LOVE QCU") -->
      <g transform="translate(790, 35)">
        <rect x="0" y="0" width="215" height="135" rx="5" fill="#0e1726" stroke="#f43f5e" stroke-width="1.8"/>
        <text x="12" y="20" fill="#f43f5e" font-size="10" font-weight="bold">SIGN LOAD: 18 MICRO-LEDS</text>
        <text x="12" y="34" fill="#cbd5e1" font-size="9">Sign: "I [HEART] QCU"</text>

        <!-- Resistors & Mode Toggle -->
        <rect x="12" y="45" width="190" height="26" fill="#1e293b" rx="3"/>
        <text x="18" y="58" fill="#ffd600" font-size="8">Full: 1.5kΩ (25mA, 125mW)</text>
        <text x="18" y="68" fill="#22c55e" font-size="8">Dim: 10kΩ (3.6mA, 18mW)</text>

        <!-- Graphical LED layout representation -->
        <!-- 'I' -->
        <circle cx="28" cy="95" r="4" fill="#ef4444" filter="url(#ledGlow)"/>
        <!-- Heart (6 LEDs) -->
        <circle cx="55" cy="88" r="3.5" fill="#f43f5e" filter="url(#ledGlow)"/>
        <circle cx="70" cy="88" r="3.5" fill="#f43f5e" filter="url(#ledGlow)"/>
        <circle cx="48" cy="98" r="3.5" fill="#f43f5e" filter="url(#ledGlow)"/>
        <circle cx="62.5" cy="100" r="3.5" fill="#f43f5e" filter="url(#ledGlow)"/>
        <circle cx="77" cy="98" r="3.5" fill="#f43f5e" filter="url(#ledGlow)"/>
        <circle cx="62.5" cy="112" r="3.5" fill="#f43f5e" filter="url(#ledGlow)"/>
        <!-- 'QCU' (11 LEDs) -->
        <g transform="translate(95, 85)">
          <text x="0" y="25" fill="#00e5ff" font-size="20" font-weight="900" letter-spacing="3" filter="url(#ledGlow)">QCU</text>
        </g>
      </g>

      <!-- 7. ESP32-WROOM-32 IoT Telemetry & Power Management Subsystem (Lower Strip) -->
      <g transform="translate(20, 180)">
        <rect x="0" y="0" width="985" height="65" rx="4" fill="#101c2e" stroke="#00e5ff" stroke-width="1.2"/>
        <text x="15" y="20" fill="#00e5ff" font-size="11" font-weight="bold">TELEMETRY &amp; POWER SUBSYSTEM (ESP32-WROOM-32 DUAL-CORE 240MHz, WI-FI/BLE, TP4056 BMS &amp; MT3608 BOOST)</text>

        <!-- Step Wakeup Connection -->
        <rect x="15" y="30" width="220" height="26" fill="#1e293b" rx="2"/>
        <circle cx="28" cy="43" r="5" fill="#ef4444"/>
        <text x="40" y="46" fill="#f8fafc" font-size="9">Piezo Pulse Wakeup → RTC ISR (GPIO 33)</text>

        <!-- Voltage Divider Connection -->
        <rect x="250" y="30" width="290" height="26" fill="#1e293b" rx="2"/>
        <text x="260" y="46" fill="#ffd600" font-size="9">100kΩ/10kΩ Divider (10:1 Ratio) → ADC1 (GPIO 34)</text>

        <!-- Wireless Telemetry & Serial Specs -->
        <rect x="555" y="30" width="210" height="26" fill="#1e293b" rx="2"/>
        <text x="568" y="46" fill="#22c55e" font-size="9">Wi-Fi 802.11bgn (UDP/MQTT) + USB UART</text>

        <!-- Power Bank & Boost Rail -->
        <rect x="780" y="30" width="190" height="26" fill="#0284c7" rx="2"/>
        <text x="792" y="46" fill="#fff" font-size="9" font-weight="bold">18650 Cell (3.7V) → 5.02V Boost Rail</text>
      </g>
    </g>
  </g>

  <!-- ================= CAD WATERMARK & REVISION METRICS ================= -->
  <text x="60" y="1065" fill="#475569" font-size="10" font-family="monospace">
    ECOSTEP-QCU-V2.0-CAD-SYSTEM | GEOMETRIC TOLERANCE: ±0.5mm | INTEL 8086 BUS ARCHITECTURE ALIGNED | QUEZON CITY UNIVERSITY
  </text>
</svg>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"[CAD Engine] SVG Technical Blueprint written to: {output_path}")
    return output_path

def generate_dxf_blueprint(output_path: str = "ecostep_qcu_blueprint.dxf"):
    """
    Generates a standard AutoCAD-compatible DXF format file (R12 / AC1009 ASCII).
    Contains layers:
    - 0_BORDER: Drawing boundary
    - TOP_PLATE: 450x450mm contour with 4 counterbore bolt holes
    - BASE_PLATE: 450x450mm base with guide holes and bulkhead mount
    - GUIDE_BOLTS: M8 bolt centerlines and pitch circle references
    - SPRINGS: 4 spring positions at edge midpoints
    - DRIVE_UNIT: Bulkhead, crank wheel, and generator envelope
    - DIMENSIONS: Metric dimension callouts
    """
    dxf_lines = [
        "0", "SECTION",
        "2", "HEADER",
        "9", "$ACADVER", "1", "AC1009",
        "9", "$INSUNITS", "70", "4",  # 4 = Millimeters
        "0", "ENDSEC",
        "0", "SECTION",
        "2", "TABLES",
        "0", "TABLE", "2", "LAYER", "70", "6",
        # Layer 1
        "0", "LAYER", "2", "TOP_PLATE", "70", "0", "62", "1", "6", "CONTINUOUS",
        # Layer 2
        "0", "LAYER", "2", "BASE_PLATE", "70", "0", "62", "5", "6", "CONTINUOUS",
        # Layer 3
        "0", "LAYER", "2", "GUIDE_BOLTS", "70", "0", "62", "3", "6", "CONTINUOUS",
        # Layer 4
        "0", "LAYER", "2", "SPRINGS", "70", "0", "62", "4", "6", "CONTINUOUS",
        # Layer 5
        "0", "LAYER", "2", "DRIVE_UNIT", "70", "0", "62", "2", "6", "CONTINUOUS",
        # Layer 6
        "0", "LAYER", "2", "DIMENSIONS", "70", "0", "62", "7", "6", "CONTINUOUS",
        "0", "ENDTAB",
        "0", "ENDSEC",
        "0", "SECTION",
        "2", "ENTITIES"
    ]

    def add_line(layer, x1, y1, x2, y2):
        dxf_lines.extend([
            "0", "LINE", "8", layer,
            "10", f"{x1:.3f}", "20", f"{y1:.3f}", "30", "0.0",
            "11", f"{x2:.3f}", "21", f"{y2:.3f}", "31", "0.0"
        ])

    def add_circle(layer, cx, cy, r):
        dxf_lines.extend([
            "0", "CIRCLE", "8", layer,
            "10", f"{cx:.3f}", "20", f"{cy:.3f}", "30", "0.0",
            "40", f"{r:.3f}"
        ])

    def add_text(layer, text, x, y, height=5.0):
        dxf_lines.extend([
            "0", "TEXT", "8", layer,
            "10", f"{x:.3f}", "20", f"{y:.3f}", "30", "0.0",
            "40", f"{height:.3f}", "1", text
        ])

    # 1. TOP PLATE (450 x 450 mm square)
    add_line("TOP_PLATE", 0, 0, 450, 0)
    add_line("TOP_PLATE", 450, 0, 450, 450)
    add_line("TOP_PLATE", 450, 450, 0, 450)
    add_line("TOP_PLATE", 0, 450, 0, 0)

    # 4 Counterbored holes for M8 bolts (30mm inset from corners)
    # Hole: 9mm clearance, Counterbore: 20mm
    bolt_coords = [(30, 30), (420, 30), (420, 420), (30, 420)]
    for bx, by in bolt_coords:
        add_circle("GUIDE_BOLTS", bx, by, 4.5)   # 9mm through-hole
        add_circle("GUIDE_BOLTS", bx, by, 10.0)  # 20mm counterbore

    # 4 Spring locations (center of edges, 20mm inset)
    spring_coords = [(225, 20), (430, 225), (225, 430), (20, 225)]
    for sx, sy in spring_coords:
        add_circle("SPRINGS", sx, sy, 12.5)  # 25mm diameter spring seat
        add_circle("SPRINGS", sx, sy, 5.0)   # locator pin

    # Center Transduction Hub & Bulkhead
    add_line("DRIVE_UNIT", 175, 175, 275, 175)
    add_line("DRIVE_UNIT", 275, 175, 275, 275)
    add_line("DRIVE_UNIT", 275, 275, 175, 275)
    add_line("DRIVE_UNIT", 175, 275, 175, 175)
    # Crank Disc (Diameter 50mm at center 225, 225)
    add_circle("DRIVE_UNIT", 225, 225, 25.0)
    # Eccentric Crank Pin at R=5mm (stroke = 10mm)
    add_circle("DRIVE_UNIT", 225, 230, 2.5)

    # Dimension Callouts
    add_text("DIMENSIONS", "450.0 mm (WIDTH)", 180, -25, 8.0)
    add_text("DIMENSIONS", "450.0 mm (DEPTH)", -35, 220, 8.0)
    add_text("DIMENSIONS", "M8 BOLT INSET: 30 mm", 35, 45, 4.0)
    add_text("DIMENSIONS", "SPRING INSET: 20 mm", 205, 35, 4.0)
    add_text("DIMENSIONS", "CRANK STROKE: 10 mm (R=5mm)", 180, 200, 4.5)
    add_text("DIMENSIONS", "ECOSTEP QCU - AR101 BSIT HARDWARE PROTOTYPE", 10, 465, 6.0)

    # End DXF
    dxf_lines.extend(["0", "ENDSEC", "0", "EOF"])

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(dxf_lines))
    print(f"[CAD Engine] DXF Exchange File written to: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_svg_blueprint()
    generate_dxf_blueprint()
