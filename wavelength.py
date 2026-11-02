#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Frequency-to-wavelength converter (free-space approximation)."""
from __future__ import annotations
import argparse
import math
import tkinter as tk
from tkinter import ttk

SPEED_OF_LIGHT = 299_792_458.0

def wavelength_m(frequency_mhz: float) -> float:
    if not math.isfinite(frequency_mhz) or frequency_mhz <= 0:
        raise ValueError("Frequency must be a finite positive number")
    return SPEED_OF_LIGHT / (frequency_mhz * 1_000_000)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mhz", type=float, help="Print wavelength in metres instead of opening GUI")
    args = parser.parse_args()
    if args.mhz is not None:
        try:
            print(f"{wavelength_m(args.mhz):.8f} m")
        except ValueError as exc:
            parser.error(str(exc))
        return
    root = tk.Tk()
    root.title("Wavelength Calculator")
    root.geometry("460x230")
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)
    value = tk.StringVar(value="145.800")
    result = tk.StringVar()
    ttk.Label(frame, text="Frequency (MHz)").pack(anchor="w")
    entry = ttk.Entry(frame, textvariable=value)
    entry.pack(fill="x", pady=8)
    slider = ttk.Scale(frame, from_=1, to=1000, orient="horizontal")
    slider.pack(fill="x", pady=8)
    def update(*_args) -> None:
        try:
            mhz = float(value.get())
            result.set(f"Wavelength: {wavelength_m(mhz):.4f} metres")
        except ValueError as exc:
            result.set(str(exc))
    def slide(v: str) -> None:
        value.set(f"{float(v):.3f}")
    slider.configure(command=slide)
    entry.bind("<Return>", update)
    value.trace_add("write", update)
    ttk.Label(frame, textvariable=result).pack(pady=10)
    slider.set(145.8)
    update()
    root.mainloop()

if __name__ == "__main__":
    main()
