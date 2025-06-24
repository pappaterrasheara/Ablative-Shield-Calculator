# Ablative Shield Calculator

A Python tool to estimate the thickness and ablation rate of thermal protection systems (ablative shields) needed for spacecraft during atmospheric re-entry. By inputting re-entry conditions and material properties, this calculator helps aerospace engineers and students assess the required thermal protection.

---

## Table of Contents
- [Overview](#overview)  
- [Background](#background)  
- [How It Works](#how-it-works)  
- [Usage](#usage)  
- [Code Structure](#code-structure)  
- [Example](#example)  
- [Requirements](#requirements)  
- [Future Improvements](#future-improvements)  
- [License](#license)  

---

## Overview

Atmospheric re-entry generates intense heat fluxes that can damage spacecraft. Ablative shields protect by gradually eroding, absorbing and carrying away heat. This calculator estimates the required shield thickness and ablation rate based on key parameters such as re-entry velocity, heat flux, and material thermal properties.

---

## Background

An ablative shield sacrifices its surface material to protect the spacecraft structure underneath during the high thermal loads of re-entry. Knowing the ablation rate and required thickness helps optimize shield design for safety and weight efficiency.

---

## How It Works

1. The user inputs:
   - Re-entry velocity (m/s)  
   - Heat flux (W/m²)  
   - Material properties (e.g., ablation enthalpy, density)

2. The program calculates:
   - Ablation rate based on heat flux and material enthalpy  
   - Required shield thickness to survive the re-entry heating duration

3. Outputs are presented clearly for design analysis.

---

## Usage

Run the script using Python 3:

```bash
python ablative_shield_calc.py
